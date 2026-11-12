# mis-skills

Skills de Claude para trabajo en Claude Web Projects. Este repositorio es la única fuente de verdad: se edita aquí, nunca directo en Claude.

| Skill | Versión | Para qué sirve | Activación |
|---|---|---|---|
| cave-planificacion | 1.6.0 | Analiza y entrega un plan o microplan aprobable. Recibe CIERRE, HALLAZGOS, PRUEBAS, CONTEXTO VERIFICADO, DEPS y DOCS. No toca código. | `/cave-planificacion` |
| cave-codeo | 1.6.1 | Implementa y verifica solo lo aprobado, cambio mínimo. | `/cave-codeo` |
| cave-pruebas | 1.0.0 | Escribe y ejecuta pruebas sobre código existente, sin tocar producción. | `/cave-pruebas` |
| cave-seguridad | 1.0.1 | Auditoría de seguridad y privacidad, solo lectura. | `/cave-seguridad` |
| cave-mapa | 1.0.0 | Explora un proyecto en solo lectura y entrega el bloque CONTEXTO VERIFICADO para el plan. | `/cave-mapa` |
| cave-deps | 1.0.0 | Actualiza dependencias por grupos, solo manifiestos y lockfiles, con línea base y reversión. | `/cave-deps` |
| cave-docs | 1.0.0 | Crea `DOCUMENTACION.md` (convención y mapa de docs) y sincroniza la documentación tras cada cambio. | `/cave-docs` |
| cave-release | 1.0.0 | Versión, changelog y comandos de commit, tag y push. No publica. | `/cave-release` |

## Flujo

planificación → codeo → pruebas → seguridad → docs → release. Cada paso va en un chat separado.

- Proyecto nuevo o desconocido: `/cave-mapa` antes de planificar; su bloque va en "2. Contexto verificado" del plan.
- Actualizar dependencias: planificación → `cave-deps` (en lugar de codeo) → pruebas → seguridad.
- Documentación: `/cave-docs init` una vez para crear `DOCUMENTACION.md`; luego `/cave-docs` tras cada cambio visible y antes de release.

- Lo que `cave-codeo` entrega (CIERRE), `cave-pruebas` (PRUEBAS), `cave-seguridad` (HALLAZGOS), `cave-mapa` (CONTEXTO VERIFICADO), `cave-deps` (DEPS) y `cave-docs` (DOCS) se pega en `/cave-planificacion`, que lo convierte en el siguiente microplan.
- Con veredicto `BLOQUEADO` de `cave-seguridad` no se llega a `cave-release`.
- Tras corregir hallazgos, se reaudita con `/cave-seguridad`.

## Formatos compartidos entre skills

Cada skill se sube sola a Claude, así que algunos textos viven en dos sitios. Al editar uno, editar el otro:

| Texto | Fuente | Copia |
|---|---|---|
| Formato del bloque CIERRE | `cave-codeo/references/cierre.md` | lista de campos en `cave-planificacion/references/modo-plan.md` |
| Formato CONTEXTO VERIFICADO | `cave-mapa/references/formato.md` | lista de campos en `cave-planificacion/references/continuidad.md` |
| Formatos DEPS y DOCS | `cave-deps/references/cierre.md`, `cave-docs/references/cierre.md` | lista de campos en `cave-planificacion/references/continuidad.md` |
| `reglas-stack.md` (idéntico) | `cave-codeo/references/` | `cave-planificacion/references/` |

## Actualizar una skill en Claude web

1. Edita la skill en el repo y sube `metadata.version` en su `SKILL.md`.
2. Anota el cambio en `CHANGELOG.md` y haz commit.
3. Ejecuta `./build.sh` (o `./build.sh cave-codeo`) para generar `dist/<skill>.zip`.
4. Claude web → Configuración → Capabilities → Skills → sube el `.zip`. Si no permite reemplazar, elimina la anterior y sube la nueva.
5. Verifica en un chat nuevo: activa la skill y pregunta qué versión está usando.
6. Si es una versión estable: `git tag cave-codeo-v1.6.1 && git push --tags`.

## Reglas para no tener problemas

- El zip lleva la carpeta de la skill en la raíz (`cave-codeo/SKILL.md`), `build.sh` ya lo hace.
- No cambies el `name` del frontmatter entre versiones.
- Cambia el `description` solo si es necesario y vuelve a probar el activador.
- Nunca guardes secretos dentro de una skill.
