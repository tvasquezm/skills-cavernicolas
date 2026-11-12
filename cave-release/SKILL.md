---
name: cave-release
metadata:
  version: "1.0.0"
description: "Preparación de lanzamientos para Claude Web Projects: determina la versión semántica a partir de los cambios reales, redacta changelog y notas de versión, sincroniza los archivos de versión y entrega los comandos exactos de commit, tag y push que ejecuta el usuario. No publica. Activar con /cave-release. Va al final del flujo, tras /cave-codeo, /cave-pruebas y /cave-seguridad."
---

# CAVE RELEASE

## Misión
Preparar un lanzamiento versionado y verificable: decidir la versión, documentar los cambios y dejar listos los comandos. **No publicar.** El commit, el tag y el push los ejecuta el usuario.

## Puerta de entrada
Antes de editar deben existir: (1) el rango de cambios identificado (último tag o versión anterior hasta el estado actual), (2) la versión propuesta con su razón, y (3) aprobación explícita del usuario sobre ese plan de release. Un plan sin esa palabra no está aprobado.
Estado previo que se revisa y se reporta, no se asume:
- Veredicto de `cave-seguridad`: con `BLOQUEADO` no se prepara el release; se informa y se detiene.
- Pruebas y verificaciones requeridas: fallidas u omitidas pasan a `Reservas` y exigen aceptación expresa del usuario.
- Árbol de trabajo con cambios ajenos al release: se señalan y no se incluyen.

## Límites duros
- Edita solo archivos de versión, `CHANGELOG`, notas de versión y los enlaces de comparación. Nunca código, dependencias, configuración ni pruebas.
- No hagas commits, tags, push, merges, rebase ni publiques releases. No ejecutes acciones destructivas de Git.
- No inventes cambios: cada entrada del changelog se respalda en un commit o diff real.
- No expongas secretos. No detalles en notas públicas una vulnerabilidad aún sin corregir o sin aviso coordinado.
- No reescribas el historial del changelog: solo agrega la versión nueva.
- No cambies la versión en un archivo sin confirmar que esa es su fuente real.

## Flujo
1. Rango: último tag o versión anterior hasta `HEAD` con comandos de solo lectura (`git describe --tags --abbrev=0`, `git log <tag>..HEAD`, `git diff --stat <tag>..HEAD`). Sin Git, pide el dato imprescindible.
2. Clasifica los cambios (`changelog`) y detecta los que rompen compatibilidad.
3. Propón la versión (`versionado`): una opción con su razón.
4. Presenta el plan de release y detente hasta la aprobación:
   - `Versión:` anterior -> nueva y por qué.
   - `Archivos:` los que se editarán, confirmados.
   - `Cambios:` entradas del changelog en borrador.
   - `Reservas:` pruebas o controles pendientes, o `ninguna`.
5. Con aprobación: edita, verifica la consistencia (todas las apariciones de la versión coinciden, fecha, enlaces) y entrega los comandos.

## Repositorio de skills
Si el repositorio contiene `SKILL.md`, la versión es por skill, con su propio tag. Detalle en `skills-repo`.

## Cierre
Solo lo que el usuario debe ejecutar: `Ejecuta en tu equipo:` y el bloque de comandos (`cierre`), con los archivos exactos y el mensaje de commit, el tag anotado y el push. Debajo, una línea con cómo revertir. Si hay reservas aceptadas, una frase. Sin introducción ni conclusión. Español, telegráfico.

## Qué leer (`references/*.md`, una vez por chat y solo si aplica)
- Elegir versión: `versionado`
- Clasificar y redactar: `changelog`
- Repositorio con skills: `skills-repo`
- Antes de entregar comandos: `cierre`
