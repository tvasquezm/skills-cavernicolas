# Actualización y verificación

## Por grupo aprobado
1. Anota el estado previo (`git status`, hash de `HEAD`, copia mental de los archivos a tocar). Si hay cambios del usuario en manifiestos o lockfile, detente.
2. Actualiza solo los paquetes del grupo, con el comando del gestor y la versión exacta del plan (`npm install paquete@x.y.z`, `pnpm update paquete@x.y.z`, `pip install paquete==x.y.z` más el archivo de requisitos, `cargo update -p`, `go get paquete@vX`). Scripts de instalación deshabilitados si el gestor lo permite.
3. Diff real (`git diff --stat` y `git diff` del manifiesto): solo los paquetes del grupo y los cambios esperados del lockfile. Lista las transitivas nuevas y las que traen `postinstall`. Un cambio inesperado en rangos, `engines` o registros detiene el grupo.
4. Verifica con los mismos controles de la línea base, en este orden: instalación congelada limpia, build o compilación, tipos, lint, pruebas focales de lo que usa el paquete y luego la suite si el riesgo lo justifica.
5. Compara con la línea base: lo que era verde sigue verde. Una falla nueva es de la actualización; una falla que ya estaba roja no se arregla ni se atribuye.

## Si falla por la actualización
- Un solo intento alternativo permitido por el plan (otra versión destino dentro del mismo grupo). Sin esa opción, no improvises.
- Si persiste: revierte ese grupo restaurando manifiesto y lockfile al estado previo, sin tocar cambios ajenos, y vuelve a correr la línea base para confirmar el retorno.
- Registra `Ruptura: <paquete> <versión>: qué falla, dónde, comando que lo reproduce`. Queda como pendiente para `cave-planificacion`; no se corrige aquí.

## Avisos y cobertura
Tras actualizar, vuelve a consultar el aviso que motivó el cambio con la fuente real (OSV, GitHub Advisory, avisos del mantenedor) y registra fuente y fecha. Sin web: `por verificar` y comando local. Un aviso se da por resuelto solo si la versión instalada queda fuera del rango afectado, comprobada en el lockfile.

## Reglas
- Una verificación requerida `OMITIDO` deja el grupo en `ejecutado, por verificar`, no cerrado.
- Nunca afirmes que algo pasó si no se ejecutó.
- Si la actualización exige versión de runtime nueva (`engines`), es un `major` de entorno: detente y pide decisión.
- Después de un cambio de dependencias que toca seguridad, el flujo sigue con `/cave-pruebas` y `/cave-seguridad`.
