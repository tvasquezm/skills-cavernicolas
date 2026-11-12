# Cierre (`/chk`)

Leer solo cuando el usuario pide `/chk` o un informe. Evidencia real, no de memoria: `git status`, `git diff --stat` y el resultado de cada comando. Sin valores de `.env` ni claves.

```
PRUEBAS - <proyecto>
Fecha:
Alcance: comportamiento o módulo probado
Archivos de prueba: rutas nuevas o modificadas
Casos: feliz N | bordes N | error N | negativos de seguridad N | regresión N
Verificación: ejecutada: comando -> resultado | fallida: ... | omitida: motivo + comando local
Fallan por la razón correcta: sí | por verificar: motivo
Hallazgos de código: ninguno | - qué falla, dónde, comando que lo reproduce (no corregido)
Pendientes: ninguno | - A (incluye lo fuera de alcance)
```
Con algo omitido o fallido el trabajo queda `ejecutado, por verificar`; no lo presentes como cerrado. Cierra con una línea: `Pega este bloque en /cave-planificacion o /cave-seguridad según corresponda.`
