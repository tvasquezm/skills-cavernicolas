# Cierre

Último paso. Verifica antes de entregar los comandos: rama actual, remoto y estado con `git status`; rutas exactas editadas con `git diff --stat`. Solo se agregan por nombre los archivos del release, nunca `git add .` si hay cambios ajenos.

## Bloque de comandos
```
Ejecuta en tu equipo:
git add <archivos exactos>
git commit -m "chore(release): vX.Y.Z"
git tag -a vX.Y.Z -m "vX.Y.Z"
git push && git push origin vX.Y.Z
```
En un repositorio de skills, el tag y el commit son por skill (`<skill>-vX.Y.Z`) y se añade `./build.sh <skill>`.
Si el proyecto publica GitHub Releases, una línea más: `gh release create vX.Y.Z --notes-file <archivo>`. Si no se sabe, no se agrega.

## Líneas finales
- `Revertir:` `git revert <commit>` y una versión parche nueva. El tag publicado no se borra.
- `Reservas aceptadas:` solo si las hay, en una frase.
- Si el estado previo no se pudo comprobar (sin Git, sin veredicto de seguridad, pruebas sin ejecutar), dilo antes del bloque y no lo presentes como listo.

## Lista previa (interna, no se imprime)
Rama correcta · árbol limpio salvo el release · veredicto de seguridad no `BLOQUEADO` · pruebas requeridas ejecutadas · versión igual en todas las fuentes · changelog con fecha de hoy · tag aún inexistente (`git tag -l`).
