# Changelog

Formato: versión por skill. Subir la versión en `metadata.version` del `SKILL.md` en cada cambio.

## cave-planificacion
- 1.6.0 — `continuidad` incorpora la recepción de CONTEXTO VERIFICADO (`cave-mapa`), DEPS (`cave-deps`) y DOCS (`cave-docs`). `modo-plan` indica que el contexto de `cave-mapa` se pega tal cual.
- 1.5.0 — `continuidad` incorpora la recepción de HALLAZGOS (`cave-seguridad`) y PRUEBAS (`cave-pruebas`). El formato CIERRE tiene una sola fuente (`cave-codeo`); `modo-plan` solo lista los campos.
- 1.4.0 — versión inicial del repositorio.

## cave-codeo
- 1.6.1 — `cierre` declara que el bloque CIERRE es la fuente única del formato.
- 1.6.0 — versión inicial del repositorio.

## cave-pruebas
- 1.0.0 — versión inicial.

## cave-seguridad
- 1.0.1 — `privacidad` ya no fija fechas de vigencia de la Ley 21.719: se consulta el estado vigente.
- 1.0.0 — versión inicial.

## cave-release
- 1.0.0 — versión inicial.

## cave-mapa
- 1.0.0 — versión inicial.

## cave-deps
- 1.0.0 — versión inicial.

## cave-docs
- 1.0.0 — versión inicial.

## cave-diseno
- 1.0.0 — versión inicial. Selector opcional de skills de diseño, fuera del flujo.

## diseno (20 skills incorporadas)
- 1.0.0 — se incorporan en `diseno/`: banner-design, brand, brandkit, design, design-system, design-taste-frontend, full-output-enforcement, gpt-taste, high-end-visual-design, image-to-code, imagegen-frontend-mobile, imagegen-frontend-web, impeccable (4.5.0), industrial-brutalist-ui, minimalist-ui, redesign-existing-projects, slides, stitch-design-taste, ui-styling, ui-ux-pro-max. Se agrega `metadata.version: "1.0.0"` a las 13 que no tenían. `build.sh` empaqueta también `diseno/*`.
