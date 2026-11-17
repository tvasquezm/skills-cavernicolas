#!/usr/bin/env python3
"""Verifica las referencias de un plan al código. Solo lectura, sin red.

Uso: python3 verificar_anclas.py PLAN.md RAIZ_DEL_PROYECTO [--json]

Clasifica cada referencia entre comillas invertidas del plan:
  archivo   -> debe existir (o su carpeta, si la fase lo crea)
  selector  -> selector CSS que debe aparecer en algún .css
  nombre    -> función, componente, variable o clase que debe aparecer en el código
y detecta citas por número de línea, que el plan no debe usar.
"""
import json, os, re, sys

SKIP_DIRS = {'node_modules', '.git', 'dist', 'build', 'coverage', '.next', '.turbo', '__pycache__'}
TEXT_EXT = ('.ts', '.tsx', '.js', '.jsx', '.mjs', '.css', '.prisma', '.sql', '.yml', '.yaml', '.json', '.md', '.html', '.example')
NEW_HINT = re.compile(r'\((nuevo|nueva)\)|\bcrea(r|s)?\b|\bagrega(r|s)?\b|\bProduce\b|\bproduce\b|\bnuevo\b|\bnueva\b', re.I)
FILE_RE = re.compile(r'^[\w@./-]+\.(tsx?|jsx?|mjs|css|md|ya?ml|json|prisma|sql|py|html)$')
SEL_RE = re.compile(r'^(:root[\w\[\]=\'"-]*|\.[A-Za-z][\w-]*(\.[A-Za-z][\w-]*)*(:[\w-]+(\([^)]*\))?)*)$')
NAME_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]{3,})(\(.*\))?$')
LINE_RES = [
    re.compile(r'[\w./-]+\.(?:tsx?|jsx?|css|md|ya?ml|json|prisma|sql):\d+'),
    re.compile(r'\blíneas? ~?\d+', re.I),
    re.compile(r'\bl\.\d+'),
    re.compile(r'cerca de la línea', re.I),
]
IGNORAR = ('PLAN_', '/tmp/', '.env')
NEG_HINT = re.compile(r'no existe|no tiene|no hay|sin versión|no usa|ya no', re.I)
COMMON = {'true', 'false', 'null', 'undefined', 'string', 'number', 'boolean', 'void', 'async', 'await', 'return',
          'import', 'export', 'const', 'default', 'ADMIN', 'DOCENTE', 'ESTUDIANTE', 'PENDIENTE', 'ACEPTADO'}


def index_project(root):
    files, text = [], {}
    for d, dirs, names in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for n in names:
            p = os.path.join(d, n)
            rel = os.path.relpath(p, root).replace(os.sep, '/')
            files.append(rel)
            if n.endswith(TEXT_EXT) and os.path.getsize(p) < 3_000_000:
                try:
                    text[rel] = open(p, encoding='utf-8', errors='ignore').read()
                except OSError:
                    pass
    return files, text


def classify(tok):
    t = tok.strip()
    if any(t.startswith(x) or x in t for x in IGNORAR):
        return None
    if not t or t.startswith(('pnpm', 'grep', 'node', 'npm', 'python', 'git', 'cd ', 'curl', '--', '$')):
        return None
    if FILE_RE.match(t):
        return 'archivo', t
    if SEL_RE.match(t):
        return 'selector', t
    m = NAME_RE.match(t)
    if m:
        n = m.group(1)
        if n in COMMON:
            return None
        mixed = bool(re.search(r'[a-z]', n) and re.search(r'[A-Z]', n))
        const = '_' in n and n.upper() == n
        if mixed or const or t.endswith(')'):
            return 'nombre', n
    return None


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    plan_path, root = sys.argv[1], sys.argv[2]
    as_json = '--json' in sys.argv
    plan = open(plan_path, encoding='utf-8').read().split('\n')
    files, text = index_project(root)
    css = {k: v for k, v in text.items() if k.endswith('.css')}
    allsrc = '\n'.join(text.values())
    res = {'verificadas': [], 'nuevas': [], 'no_encontradas': [], 'ausentes_esperadas': [], 'ambiguas': [], 'lineas': []}
    seen = set()
    for i, line in enumerate(plan, 1):
        for rx in LINE_RES:
            for m in rx.finditer(line):
                res['lineas'].append({'plan_linea': i, 'texto': m.group(0)})
        for tok in re.findall(r'`([^`\n]+)`', line):
            c = classify(tok)
            if not c:
                continue
            kind, val = c
            key = (kind, val)
            if key in seen:
                continue
            seen.add(key)
            nuevo = bool(NEW_HINT.search(line))
            item = {'tipo': kind, 'ancla': val, 'plan_linea': i}
            if kind == 'archivo':
                hits = [f for f in files if f == val or f.endswith('/' + val)]
                if len(hits) == 1:
                    res['verificadas'].append(item)
                elif len(hits) > 1:
                    item['coincidencias'] = hits[:5]; res['ambiguas'].append(item)
                else:
                    parent = os.path.dirname(val)
                    dir_ok = bool(parent) and any(f.startswith(parent + '/') or ('/' + parent + '/') in f for f in files)
                    (res['nuevas'] if (nuevo or dir_ok) else res['no_encontradas']).append(item)
            elif kind == 'selector':
                core = val.split(':')[0] if not val.startswith(':root') else val
                found = any(core in v for v in css.values()) or (core.startswith('.') and re.search(r'(?<![\w-])' + re.escape(core[1:]) + r'(?![\w-])', allsrc) is not None)
                (res['verificadas'] if found else (res['nuevas'] if nuevo else res['no_encontradas'])).append(item)
            else:
                found = re.search(r'(?<![\w])' + re.escape(val) + r'(?![\w])', allsrc) is not None
                (res['verificadas'] if found else (res['ausentes_esperadas'] if NEG_HINT.search(line) else (res['nuevas'] if nuevo else res['no_encontradas']))).append(item)
    if as_json:
        print(json.dumps(res, ensure_ascii=False, indent=1)); return
    print(f"ANCLAS - {os.path.basename(plan_path)}")
    print(f"Verificadas: {len(res['verificadas'])} | Nuevas (las crea el plan): {len(res['nuevas'])} | "
          f"No encontradas: {len(res['no_encontradas'])} | Ausentes esperadas: {len(res['ausentes_esperadas'])} | Ambiguas: {len(res['ambiguas'])} | Citas por línea: {len(res['lineas'])}")
    for titulo, clave in (('No encontradas', 'no_encontradas'), ('Ausentes esperadas (el plan dice que no existen)', 'ausentes_esperadas'), ('Ambiguas', 'ambiguas'), ('Citas por línea (prohibidas)', 'lineas'), ('Nuevas', 'nuevas')):
        if res[clave]:
            print(f"\n## {titulo}")
            for it in res[clave]:
                if clave == 'lineas':
                    print(f"- plan:{it['plan_linea']} | {it['texto']}")
                else:
                    extra = f" | en: {', '.join(it['coincidencias'])}" if 'coincidencias' in it else ''
                    print(f"- plan:{it['plan_linea']} | {it['tipo']} | {it['ancla']}{extra}")


if __name__ == '__main__':
    main()
