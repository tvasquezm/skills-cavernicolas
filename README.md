# mis-skills

Skills de Claude para trabajo en Claude Web Projects. Este repositorio es la única fuente de verdad: se edita aquí, nunca directo en Claude.

| Skill | Versión | Para qué sirve | Activación |
|---|---|---|---|
| cave-planificacion | 1.4.0 | Analiza y entrega un plan o microplan aprobable. No toca código. | `/cave-planificacion` |
| cave-codeo | 1.6.0 | Implementa y verifica solo lo aprobado, cambio mínimo. | `/cave-codeo` |
| cave-seguridad | (pendiente) | Auditoría de seguridad y privacidad, solo lectura. | `/cave-seguridad` |

Flujo: planificación → codeo → seguridad (puerta final antes de commit o PR). Cada paso va en un chat separado.

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
