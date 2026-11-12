# Inventario y plan

## Comandos de solo lectura por gestor
Verifica el gestor real por el lockfile antes de escribirlos.
- npm: `npm outdated`, `npm ls <paquete>`, `npm view <paquete> versions time`. pnpm: `pnpm outdated`. yarn: `yarn outdated` / `yarn npm audit`. 
- pip: `pip list --outdated`, `pip-audit`. uv: `uv pip list --outdated`. poetry: `poetry show --outdated`.
- Go: `go list -u -m all`, `govulncheck ./...`. Cargo: `cargo outdated`, `cargo audit`.
- Multi: `osv-scanner`, `trivy fs .`.
Corre aquí solo lo que exista y no escriba en el proyecto. Sin red o herramienta: `OMITIDO` y comando en `Ejecuta en tu equipo:`.

## Clasificación
Por paquete: `actual -> destino (tipo)`. Tipos: `patch`, `minor`, `major`; `0.x` se trata como `major` en cualquier salto de minor. Marca: prod o dev, directa o transitiva, motivo (aviso `S-<n>`, abandono, pedido).

## Prioridad
1. Avisos alcanzables desde el código del proyecto (KEV, EPSS alto, `S-<n>` de `cave-seguridad`).
2. Patch y minor de producción.
3. Dev y herramientas de build.
4. Major, uno por vez, con valor claro.
Un paquete abandonado o sin mantenimiento se señala, no se reemplaza aquí: reemplazar es un microplan de `cave-codeo`.

## Notas de ruptura
Para cada `major` (y minor de `0.x`): lee el changelog o la guía de migración del paquete. Anota qué cambia y dónde puede impactar en el proyecto (grep de uso). Sin acceso: `por verificar` y no se agenda como seguro.

## Transitivas
Una vulnerabilidad en una transitiva se resuelve actualizando el padre. `overrides` o `resolutions` solo con aprobación expresa y con la razón escrita.

## Formato del plan
```
PLAN DEPS - <proyecto>
Gestor: ... | Línea base: verde | roja: ... | por verificar
Grupo 1 - <motivo> | riesgo: bajo|medio|alto
- paquete: actual -> destino (tipo) | prod|dev | aviso: S-n|ninguno
Ruptura esperada: ninguna | - qué cambia y dónde impacta
Verificación: comandos -> resultado esperado
Reversión: restaurar manifiesto y lockfile del estado previo
Grupo 2 ...
Fuera: paquetes que no se actualizan y por qué
¿Apruebas este plan? Se ejecuta un grupo por vez.
```
