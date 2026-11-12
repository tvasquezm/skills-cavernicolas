# Cierre (`/chk`)

Leer solo cuando el usuario pide `/chk` o un informe. Evidencia real, no de memoria: `git status`, `git diff --stat` y el resultado de cada comando. Sin tokens ni credenciales de registros.

```
DEPS - <proyecto>
Fecha:
Gestor: ... | lockfile: ...
Motivo: seguridad S-<n> | mantenimiento | pedido
Línea base: verde | roja: ...
Actualizados: paquete antes -> después (tipo)
Sin actualizar: ninguno | - paquete: motivo (ruptura, peer, no aprobado)
Verificación: ejecutada: comando -> resultado | fallida: ... | omitida: motivo + comando local
Transitivas nuevas o con scripts de instalación: ninguna | - ...
Rupturas: ninguna | - paquete versión: qué falla, dónde, comando que lo reproduce (no corregido)
Avisos: resueltos: ... | por verificar: ... (fuente y fecha)
Reversión: restaurar <manifiesto> y <lockfile> al estado previo (git revert <commit> si ya hay commit)
Pendientes: ninguno | - A (incluye lo fuera de alcance)
```
Con algo omitido o fallido el trabajo queda `ejecutado, por verificar`; no lo presentes como cerrado. Cierra con una línea: `Pega este bloque en /cave-planificacion; tras actualizar, sigue /cave-pruebas y /cave-seguridad.`
