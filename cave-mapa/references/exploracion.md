# Exploración

## Orden (de lo barato a lo caro)
1. `git status`, `git branch --show-current`, `git log --oneline -5`, `git describe --tags --abbrev=0`. Sin Git: anótalo.
2. Raíz y un nivel de carpetas (`ls`, árbol de 2 niveles sin `node_modules`, `.git`, `dist`, `build`, `vendor`).
3. Manifiestos y lockfiles: `package.json`, `pnpm-lock.yaml`/`package-lock.json`/`yarn.lock`/`bun.lockb`, `pyproject.toml`, `requirements*.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, `Gemfile`, `composer.json`. El lockfile que existe define el gestor.
4. Versión de runtime: `engines`, `.nvmrc`, `.node-version`, `.python-version`, `.tool-versions`, `rust-toolchain`, `Dockerfile`.
5. Comandos: `scripts` del manifiesto, `Makefile`, `justfile`, `Taskfile`, y sobre todo lo que ejecuta el CI (`.github/workflows`, `.gitlab-ci.yml`). Si CI y scripts difieren, anota ambos y marca cuál corre el CI.
6. Configuración de calidad: lint, formateo, tipos (`eslint`, `prettier`, `tsconfig`, `ruff`, `mypy`, `.editorconfig`).
7. Entradas: `main`, `bin`, `src/index`, `app/`, `pages/`, `cmd/`, servidor, rutas, workers.
8. Datos: ORM y migraciones (`prisma/`, `migrations/`, `alembic/`), nombres de modelos principales; solo existencia.
9. Variables: `.env.example`, `.env.sample`, lecturas de `process.env`/`os.environ` con grep. **Nunca abrir `.env` real.** Solo nombres.
10. Pruebas: framework, carpeta, patrón de nombre y **una prueba existente como modelo** (ruta).
11. Documentación: `README`, `docs/`, `DOCUMENTACION.md`, `CONTRIBUTING`, `CHANGELOG`, OpenAPI.

## Convenciones: cómo inferirlas
Abre 1 o 2 archivos representativos del área, no el árbol entero. Anota solo lo que se repite: nombres de archivos y símbolos, estructura de módulos, manejo de errores, validación, estilo de imports, ubicación de pruebas. Una convención vista una sola vez es `por verificar`.

## Receta de verificación
Pasos mínimos para dejar el proyecto listo para probar en el entorno de trabajo: instalación congelada y sin scripts (`npm ci --ignore-scripts`, `pnpm install --frozen-lockfile`, `pip install -r`, etc.), generaciones necesarias (`prisma generate`, codegen), variables requeridas (nombres) y servicios que se necesitan (base de datos, cola). Estado `probada` solo con `probar`; si no, `por verificar`.

## Riesgos de arranque a señalar
Árbol sucio, sin lockfile, sin pruebas, sin CI, scripts que no existen pero se mencionan en el README, versiones de runtime incompatibles, migraciones pendientes. Una línea cada uno, sin proponer solución.
