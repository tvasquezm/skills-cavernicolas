# CIERRE (`/chk`)

Leer solo cuando el usuario pide `/chk` o llega un CIERRE o un plan al chat. Sin pedido, no se genera nada.

## `/chk`
Arma el bloque con evidencia real, no de memoria: `git status` y `git diff --stat` (sin Git, `diff -rq orig work`), el resultado de los controles y los nombres, rutas y firmas nuevos confirmados con grep sobre el código. Entrégalo como un bloque de código, sin valores de `.env` ni claves, y cierra solo con eso más una línea: `Pega este CIERRE en el chat de /cave-planificacion.`
```
CIERRE F<id> - <proyecto>
Fecha:
Hecho: qué quedó funcionando
Contratos reales: nombres, rutas, firmas y formatos exactos que quedaron
Desvíos del plan: ninguno | qué se hizo distinto y por qué
Decisiones nuevas: ninguna | decisión - por qué
Verificación: ejecutada: comando -> resultado | fallida: ... | omitida: motivo + comando local
Aprendido del entorno: nada | qué hizo falta para poder probar
Pendientes: ninguno | - A (incluye lo encontrado fuera de alcance)
```
Este bloque es la única fuente del formato CIERRE: `cave-planificacion` lo pega tal cual en `## CIERRE` de la fase. No renombres ni agregues campos. Si el formato cambia, se cambia aquí y se actualiza la lista de campos de `modo-plan` en `cave-planificacion` (solo nombres). Con algo omitido o fallido, la fase queda `ejecutada, por verificar`; no la presentes como cerrada.

## Al llegar un plan o un CIERRE
Úsalo como contexto mínimo junto con el microplan aprobado; no pidas ni resumas el plan completo. Antes de apoyarte en un Contrato que consumes, compruébalo con grep. Si difiere: una frase con la diferencia; detente solo si bloquea.
