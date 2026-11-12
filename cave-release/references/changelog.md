# Changelog y notas de versión

Formato tipo Keep a Changelog. Se agrega una sección nueva arriba; las anteriores no se tocan.

```
## [X.Y.Z] - AAAA-MM-DD
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
```
Omite las secciones vacías. Al final del archivo, los enlaces de comparación si el proyecto ya los usa (`[X.Y.Z]: <repo>/compare/vA...vX.Y.Z`); sin repositorio remoto confirmado, no los inventes.

## Clasificación
- Funcionalidad nueva compatible: `Added`. Comportamiento modificado: `Changed`. Marcado para retirar: `Deprecated`. Retirado: `Removed`. Defectos: `Fixed`. Vulnerabilidades corregidas: `Security`.
- Los cambios incompatibles se marcan `**BREAKING:**` con qué hacer para migrar.

## Redacción
- Una línea por cambio, en términos del efecto para quien usa el proyecto, no del commit.
- Agrupa commits que son un mismo cambio. Omite el ruido (merges, formato, `wip`).
- Cada entrada se respalda en un commit o diff real; si no puedes respaldarla, no entra.
- Referencias a tickets o PR solo si existen en los commits.
- Sin secretos, rutas internas sensibles ni detalle explotable de vulnerabilidades sin corregir.

## Notas de versión (si se piden)
Resumen de 2 a 4 líneas para usuarios, lo más importante primero, luego los `BREAKING` con su migración y los enlaces. Distinto del changelog: más corto y sin lista exhaustiva.
