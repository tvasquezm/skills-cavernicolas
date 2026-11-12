# Cierre (`/chk`)

Leer solo cuando el usuario pide `/chk` o un informe. Evidencia real, no de memoria: `git status`, `git diff --stat` y el resultado de cada comando. Sin valores de `.env` ni claves.

```
DOCS - <proyecto>
Fecha:
Modo: init | sync | revisar
Índice: DOCUMENTACION.md creado | actualizado | sin cambios
Documentos: DC<n> ruta - creado | actualizado | revisado sin cambios
Verificación: ejecutada: comando -> resultado | fallida: ... | omitida: motivo + comando local
Desfases: ninguno | - DC<n> doc:línea dice X; el código hace Y (archivo:línea). No corregido en el código
Por verificar: ninguno | - dato: cómo comprobarlo
Pendientes: ninguno | - A (incluye lo fuera de alcance y documentos `por crear`)
```
Con algo omitido o fallido el trabajo queda `ejecutado, por verificar`; no lo presentes como cerrado. Cierra con una línea: `Pega este bloque en /cave-planificacion; sigue /cave-release.` En `revisar`, los desfases de código van a un microplan de `cave-codeo`.
