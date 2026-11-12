# Reglas de código y entrega

Leer antes de editar. El alcance y la protección del trabajo están en `SKILL.md`.

## Código
- Revisa el proyecto real antes de tocar nada; nunca inventes archivos, APIs, funciones ni dependencias.
- Reutiliza antes de crear (busca algo equivalente) y no dupliques. Antes de sumar algo, comprueba si realmente se usa.
- Sin features extra, librerías innecesarias, código de ejemplo ni datos ficticios. Primero que funcione; no optimices prematuramente.
- Comentarios solo si el usuario los pide, son técnicamente necesarios o explican una decisión compleja no obvia.
- README, CHANGELOG, `docs/` y diagramas solo si el microplan los incluye.
- Tests: si el cambio rompe uno existente, actualízalo. Nuevos solo si el microplan los pide, con el framework que el proyecto ya usa; si cubren authz o validación, incluye el caso negativo. Un test de regresión cuenta solo si falla contra el código original y pasa contra el modificado.
- Preserva el formato de cada archivo: CRLF/LF, indentación, BOM y newline final.

## Entrega
- **Acceso directo al repositorio:** edita en el lugar; no hay entrega de archivos.
- **Proyecto subido al chat:** antes de la primera edición guarda una copia intacta en `orig` y trabaja en `work`. Al terminar, entrega como archivos descargables solo los nuevos y modificados, con su ruta relativa (varios: un zip con ellos). Nunca el proyecto entero, `node_modules`, builds, `.env` ni temporales. Un borrado va como comando en `Ejecuta en tu equipo:`.
- Respeta el formato de entrega que el usuario ya definió (archivo completo, fragmento, diff). Archivo de más de 200 líneas que no se pidió completo: diff o fragmento.
- Bloque de código que el usuario va a reemplazar: SOLO código, sin notas ni explicaciones; los comandos van fuera, en su línea.
- Un microplan de más de ~10 archivos o ~500 líneas de diff se devuelve a `cave-planificacion` para dividirlo.
