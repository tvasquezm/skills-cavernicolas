# Repositorio de skills

Cada skill tiene su versión en `metadata.version` del `SKILL.md` y su propio tag, así se actualiza solo la que cambió.

## Versión por tipo de cambio
- **MAYOR:** cambia el `name` (Claude la trata como otra skill), se elimina un comando o una puerta de entrada, o cambia de forma incompatible lo que la skill entrega o exige.
- **MENOR:** cambia el `description` (afecta cuándo se activa: hay que retestar el activador), se agrega una regla, un flujo, una referencia o un formato.
- **PARCHE:** corrección de texto, ejemplo o regla sin cambio de comportamiento.
- Un cambio de `name` se señala como riesgo antes de aprobar el release.

## Archivos
- `<skill>/SKILL.md`: subir `metadata.version`.
- `CHANGELOG.md` del repositorio: sección por skill con la versión nueva.
- `README.md`: la tabla de skills con la versión vigente.
- Referencias que citen la versión (`Skill: cave-planificacion v<versión>` y similares): confirmar que se leen de la fuente y no quedan desfasadas.

## Tags
`<skill>-vX.Y.Z` (por ejemplo `cave-codeo-v1.6.1`). Un release que toca varias skills lleva un tag por skill.

## Paquete
Tras el push, `./build.sh <skill>` genera `dist/<skill>.zip` con la carpeta de la skill en la raíz, y ese zip se sube a Claude web. Verifica en un chat nuevo preguntando qué versión usa la skill. Si el usuario publica Releases en GitHub, el zip se adjunta al release de ese tag.

## Revertir
Un tag publicado no se borra. Se vuelve a una versión anterior con un nuevo commit que restaure los archivos de la skill y una versión parche nueva.
