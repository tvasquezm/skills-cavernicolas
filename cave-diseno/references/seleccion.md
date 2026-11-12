# Selección de skills de diseño

Las skills viven en `diseno/` del repositorio. Por defecto se instalan solo las 5 recomendadas; el resto, solo si la tarea lo pide.

## Por tipo de tarea
| Tarea | Base | Complemento |
|---|---|---|
| Interfaz nueva (web, app, dashboard) | `impeccable` | `ui-ux-pro-max` |
| Rediseñar o mejorar un proyecto existente | `redesign-existing-projects` | `impeccable` |
| Auditar o criticar una interfaz | `impeccable` (modo audit o critique) | `ui-ux-pro-max` |
| Que el resultado no salga genérico | `design-taste-frontend` | `impeccable` |
| Entregar código completo, sin recortes | `full-output-enforcement` | la base de la tarea |
| Sistema de tokens y componentes | `design-system` | `ui-styling` |
| Tailwind, shadcn/ui, componentes | `ui-styling` | `design-system` |
| Presentación HTML | `slides` | `design-system` |
| Marca, voz y guías | `brand` | `design-system` |
| Banner | `banner-design` | `brand` |

## Estilo (elegir una sola)
`minimalist-ui` (editorial, monocromo cálido) | `high-end-visual-design` (agencia, premium) | `industrial-brutalist-ui` (denso, datos, terminal) | `gpt-taste` (editorial con movimiento GSAP) | `stitch-design-taste` (genera `DESIGN.md` para Google Stitch).
Sin estilo pedido, no añadas ninguno: la base decide.

## Solo con generador de imágenes (no usar en chat)
`brandkit`, `image-to-code`, `imagegen-frontend-web`, `imagegen-frontend-mobile`. Si la tarea las pide, di que no aplican aquí y usa la base de la tabla.

## Solapes
- `design` agrupa brand, banner, slides y design-system y usa APIs externas: preferir las skills sueltas.
- `design-taste-frontend`, `high-end-visual-design` y `gpt-taste` se pisan: nunca juntas.
- `full-output-enforcement` es compatible con cualquiera y no cuenta como estilo.
