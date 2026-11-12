# Versionado

Versionado semántico `MAYOR.MENOR.PARCHE`. Lo decide el cambio de mayor impacto del rango, no la cantidad.

- **MAYOR:** rompe compatibilidad (quita o renombra algo público, cambia un contrato, una migración que exige acción del usuario).
- **MENOR:** agrega funcionalidad compatible o depreca algo.
- **PARCHE:** correcciones compatibles, sin funcionalidad nueva.
- Cambios internos sin efecto observable (refactor, pruebas, documentación): sin release propio, o parche si el usuario lo pide.

## Reglas
- `0.y.z`: la API aún no es estable; un cambio incompatible puede subir `y`. Dilo si aplica.
- Prelanzamientos: `X.Y.Z-rc.1`, `-beta.1`. No se reutilizan ni se mueven.
- **Un tag publicado no se reescribe ni se borra.** Un error se corrige con una versión nueva.
- Un arreglo de seguridad va como PARCHE como mínimo, con aviso en `Security` cuando ya esté corregido.
- Duda entre dos niveles: elige el mayor y dilo en una frase.

## Fuente de la versión
Antes de editar localiza todas las apariciones reales (`package.json`, `pyproject.toml`, `Cargo.toml`, `*.csproj`, `version.*`, `metadata.version` en `SKILL.md`, constantes en código, imágenes, documentación). Se editan solo las que el proyecto usa como fuente; las derivadas se generan. Al terminar, busca de nuevo la versión anterior y confirma que no quedan apariciones sin explicar.
Los lockfiles que registran la versión del propio paquete solo se tocan si el proyecto lo requiere; si es así, se dice y se entrega el comando para regenerarlos en `Ejecuta en tu equipo:`.
