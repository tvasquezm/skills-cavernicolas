# mis-skills

Skills de Claude para trabajo en Claude Web Projects. Este repositorio es la única fuente de verdad: se edita aquí, nunca directo en Claude.

| Skill | Versión | Para qué sirve | Activación |
|---|---|---|---|
| cave-planificacion | 1.7.0 | Analiza y entrega un plan o microplan aprobable. Recibe CIERRE (también de otro agente de código), HALLAZGOS, PRUEBAS, CONTEXTO VERIFICADO, DEPS, DOCS y comentarios del equipo. Genera el plan para otro agente y el documento de revisión en lenguaje simple. No toca código. | `/cave-planificacion` |
| cave-anclas | 1.0.0 | Verifica en solo lectura que las referencias de un plan al código (archivos, funciones, selectores, variables) existan y apunten a un solo lugar; detecta citas por número de línea. | `/cave-anclas` |
| cave-codeo | 1.6.1 | Implementa y verifica solo lo aprobado, cambio mínimo. | `/cave-codeo` |
| cave-pruebas | 1.0.0 | Escribe y ejecuta pruebas sobre código existente, sin tocar producción. | `/cave-pruebas` |
| cave-seguridad | 1.0.1 | Auditoría de seguridad y privacidad, solo lectura. | `/cave-seguridad` |
| cave-mapa | 1.0.0 | Explora un proyecto en solo lectura y entrega el bloque CONTEXTO VERIFICADO para el plan. | `/cave-mapa` |
| cave-deps | 1.0.0 | Actualiza dependencias por grupos, solo manifiestos y lockfiles, con línea base y reversión. | `/cave-deps` |
| cave-docs | 1.0.0 | Crea `DOCUMENTACION.md` (convención y mapa de docs) y sincroniza la documentación tras cada cambio. | `/cave-docs` |
| cave-release | 1.0.0 | Versión, changelog y comandos de commit, tag y push. No publica. | `/cave-release` |
| cave-diseno | 1.1.0 | Opcional, fuera del flujo. Elige la skill de `diseno/` que corresponde a la tarea y fija una sola dirección visual, con inventario para pantallas cargadas (`reducir`), alternativas y criterios medibles. | `/cave-diseno` |

## Skills de diseño (opcionales, fuera del flujo)

Viven en `diseno/` (una carpeta por skill, nombre sin cambios). No son un paso del flujo `cave-*`: se usan solo cuando la tarea tiene diseño, y `/cave-diseno` ayuda a elegir cuál. Origen, licencias y cuáles funcionan en chat: `diseno/MANIFIESTO.md`. `./build.sh` las empaqueta junto con las `cave-*` en `dist/<skill>.zip`; también `./build.sh impeccable`.

- Instalar por defecto: `impeccable`, `ui-ux-pro-max`, `design-taste-frontend`, `redesign-existing-projects`, `full-output-enforcement`.
- Solo si la tarea lo pide: `minimalist-ui`, `high-end-visual-design`, `industrial-brutalist-ui`, `gpt-taste`, `stitch-design-taste`, `design-system`, `ui-styling`.
- Parciales en chat (necesitan generador de imágenes, APIs o red): `brandkit`, `image-to-code`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `design`, `brand`, `banner-design`, `slides`.
- Están en inglés. Las que no traían `metadata.version` quedaron en `1.0.0`; `impeccable` conserva su `version: 4.5.0` de origen.
- Sin ninguna de ellas instalada, `/cave-diseno` no entrega un bloque vacío: construye la dirección desde los tokens y capturas del proyecto y lo declara en `Fuente`.

## Flujo

planificación → anclas → codeo → pruebas → seguridad → docs → release. Cada paso va en un chat separado.

- Proyecto nuevo o desconocido: `/cave-mapa` antes de planificar; su bloque va en "2. Contexto verificado" del plan.
- Antes de ejecutar un plan (con `cave-codeo` o con otro agente de código): `/cave-anclas` con el plan y el proyecto. Sus hallazgos (anclas no encontradas, ambiguas o citas por línea) vuelven a `/cave-planificacion` para corregir el plan. Se repite al cambiar el plan, al retomarlo con el código cambiado y tras cerrar una fase.
- Plan para otro agente de código (Codex u otro): lo genera `/cave-planificacion` desde `PLAN_APROBADO.md` (referencia `para-agente`); nunca se edita aparte. El CIERRE de ese agente se pega de vuelta en `/cave-planificacion`.
- Revisión por personas no técnicas antes de ejecutar: `/cave-planificacion` genera el documento de revisión (referencia `revision-equipo`); sus comentarios se pegan de vuelta para ajustar el plan.
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
| Plantilla de CIERRE de otro agente de código | `cave-planificacion/references/para-agente.md` | lista de campos en `cave-planificacion/references/continuidad.md` |
| Formato CONTEXTO VERIFICADO | `cave-mapa/references/formato.md` | lista de campos en `cave-planificacion/references/continuidad.md` |
| Formatos DEPS y DOCS | `cave-deps/references/cierre.md`, `cave-docs/references/cierre.md` | lista de campos en `cave-planificacion/references/continuidad.md` |
| `reglas-stack.md` (idéntico) | `cave-codeo/references/` | `cave-planificacion/references/` |
| Regla "anclas por nombre, nunca por número de línea" | `cave-planificacion/SKILL.md` | `cave-planificacion/references/modo-plan.md`, `cave-planificacion/references/para-agente.md` y `cave-anclas/SKILL.md` |

## Actualizar una skill en Claude web

1. Edita la skill en el repo y sube `metadata.version` en su `SKILL.md`.
2. Anota el cambio en `CHANGELOG.md` y haz commit.
3. Ejecuta `./build.sh` (o `./build.sh cave-codeo`) para generar `dist/<skill>.zip`.
4. Claude web → Configuración → Capabilities → Skills → sube el `.zip`. Si no permite reemplazar, elimina la anterior y sube la nueva.
5. Verifica en un chat nuevo: activa la skill y pregunta qué versión está usando.
6. Si es una versión estable: `git tag cave-codeo-v1.6.1 && git push --tags`.

## Reglas para no tener problemas

- El zip lleva la carpeta de la skill en la raíz (`cave-codeo/SKILL.md`), `build.sh` ya lo hace.
- El zip debe incluir también `references/` y, en `cave-anclas`, la carpeta `scripts/` (`verificar_anclas.py`): sin el script la skill no puede verificar nada. Comprueba que `build.sh` la copia; tras `./build.sh cave-anclas`, `unzip -l dist/cave-anclas.zip` debe listar `cave-anclas/scripts/verificar_anclas.py`.
- No cambies el `name` del frontmatter entre versiones.
- Cambia el `description` solo si es necesario y vuelve a probar el activador.
- Nunca guardes secretos dentro de una skill.