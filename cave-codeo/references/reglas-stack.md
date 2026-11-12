# Migraciones y variables de entorno

Leer al tocar esquema de base de datos, migraciones o variables de entorno. Archivo compartido: copia idéntica en `cave-planificacion` y `cave-codeo`; si se edita, editar ambas. Escrito para React/Vite + NestJS + PostgreSQL; con otro stack, aplicar los mismos principios.

## Migraciones
- Nunca modificar una migración ya aplicada o mergeada: todo cambio va en una migración nueva (también para revertir).
- Las destructivas (`DROP`, `TRUNCATE`, borrar columna o tabla, cambiar un tipo con pérdida) exigen su propio microplan aprobado, con riesgo ALTO y reversión. Quien ejecuta no las aplica si el microplan no las incluye de forma expresa.
- Si el cambio rompe código en producción (renombrar o borrar lo que la app aún lee): dos entregas. Primero se agrega lo nuevo y el código deja de usar lo viejo; después, otra migración elimina lo viejo.
- No inventar tablas, columnas ni la herramienta de migraciones: leerlas del proyecto. El estado real de lo aplicado solo lo conoce la base; si no se puede consultar, decirlo.
- `CREATE INDEX CONCURRENTLY` no corre dentro de una transacción: verificar cómo la herramienta del proyecto envuelve las migraciones.
- Seeds y datos de prueba: fuera de las migraciones de esquema.

## Variables de entorno
- Nunca hardcodear secrets ni connection strings. Variable nueva: se declara en `.env.example` (sin valor real) a la vez que se usa, y se anota en el microplan y en `Contratos reales` del CIERRE.
- No imprimir valores reales de `.env`; para depurar, comprobar solo si está definida.
- Vite: lo que lleva prefijo `VITE_` queda público en el bundle; un secreto nunca lo lleva.
- NestJS: si el proyecto ya valida su configuración al arrancar, agregar la variable a ese esquema; si no, no introducir validación de paso.
- "Pasa local, falla en CI" suele ser una variable que falta en el workflow.
