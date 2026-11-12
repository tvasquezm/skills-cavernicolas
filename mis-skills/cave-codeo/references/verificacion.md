# Verificación

Leer antes de cerrar. Es registro interno: no se informa en el cierre salvo fallo no resuelto u omisión sin comando local (ver `SKILL.md`).

**Sin evidencia no hay "pasó".** Cada control lleva comando real y resultado. Lo no ejecutado es `OMITIDO` con motivo y nunca cuenta como aprobado.

1. **Pruebas focales** con los scripts reales del proyecto (`package.json`, `Makefile`, pytest...). Sin suite aplicable: la comprobación mínima que demuestre el cambio (compilar, importar, correr el caso).
2. **Lint y tipos** solo los que el proyecto ya define sobre lo tocado. Falla por tu cambio: corregir. Preexistente: no tocar.
3. **Diff real:** `git status` y `git diff`; sin Git, `diff -ruN orig work`. Confirma que solo cambió lo del alcance, sin reformateos, lockfiles ni configuración no autorizados, con el formato preservado y sin temporales.
4. **Secretos:** revisa las líneas agregadas por claves, tokens, contraseñas y cadenas de conexión. Nunca imprimas el valor. Si lo introdujo el cambio, corrígelo.
5. **Seguridad**, solo si el microplan toca auth o permisos, datos personales, entrada hacia SQL/shell/archivos/HTML/URLs, uploads, cookies/CORS/headers, criptografía o migraciones: prueba el control que el microplan declaró, con el caso negativo (acceso cruzado o entrada inválida).

**Si falla por el cambio:** corrige dentro del alcance y repite ese control; al tercer intento sin resultado, regla de 3 (`debug`).
**Entorno de verificación.** Usa primero la receta del plan (`Contexto verificado`). Si falta una dependencia, instálala desde el lockfile (instalación congelada y sin scripts, sin tocar `package.json` ni lockfiles) y genera lo que el proyecto necesite para correr (por ejemplo `prisma generate`), sin entregar esos artefactos. Si no hay red o herramienta: no inventes; registra `OMITIDO`, sigue con alternativas útiles y deja el comando en `Ejecuta en tu equipo:`.
**Una verificación requerida `OMITIDO` deja la fase en `ejecutada, por verificar`**, no cerrada: va en `Verificación` del CIERRE. Lo que descubras para que el entorno funcione, anótalo en `Aprendido del entorno`.
**Arreglo de un error:** se da por arreglado solo si el síntoma se reprodujo antes (falla) y después (pasa).
