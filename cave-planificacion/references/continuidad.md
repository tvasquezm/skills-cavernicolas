# SPIKE, retomar y CIERRE

Leer ante "¿se puede...?", al retomar, o al recibir un CIERRE de `cave-codeo`.

## SPIKE
`Respuesta: sí | no | depende - evidencia - costo estimado`. Se responde leyendo el proyecto o la documentación; esta skill no ejecuta pruebas. Si hace falta ejecutar algo, se redacta como microplan de una prueba descartable para `cave-codeo`.

## Retomar
Entrada: `PLAN_APROBADO.md` (ESTADO ACTUAL), la fase en curso y, si no hay plan global, el CIERRE más reciente. No re-mapear ni re-preguntar lo decidido.
1. Si `En curso` está en `microplan aprobado` o `ejecutada, por verificar` y no hay CIERRE: `Falta el CIERRE de F<id>: pide /chk en cave-codeo y pégalo aquí.` Es la única pregunta.
2. Verificación ligera, solo lectura: comprueba con grep los Contratos que la siguiente fase consume y los datos `por verificar` de su bloque. Una diferencia se señala antes de planear.
3. Si `Verificación pendiente` no está vacía y toca lo que viene, el microplan empieza por correrla o por pedirle al usuario el resultado.
4. Si la fase está en `esbozo`, detállala (ver `modo-plan`) antes del microplan.
```
RETOMAR
Fase: F<id> - estado
Base: confirmada | por verificar (motivo)
Contratos consumidos: coinciden | difieren: ruta :: firma
Pendiente: verificación ... | decisiones abiertas ...
Siguiente: microplan de F<id>
```
`Base: confirmada` solo con evidencia. Termina con el microplan y su pregunta de aprobación.

## Al recibir un CIERRE
1. Pegarlo en `## CIERRE` de `FASE_<id>.md` (o en la fase, si el plan es de archivo único).
2. Estado de la fase: `cerrada` solo si la verificación requerida se ejecutó. Con algo `omitido` o `fallida`: `ejecutada, por verificar`, y el comando pasa a `Verificación pendiente` del Estado.
3. `Contratos reales` mandan sobre `Produce`. Actualiza el `Consume` de las fases siguientes que usen los nombres planeados.
4. `Desvíos del plan`: corrige el `## PLAN` de la fase en el mismo paso (el plan refleja la realidad) y registra en Historial qué cambió y por qué.
5. `Aprendido del entorno`: promuévelo a `2. Contexto verificado` (receta de verificación).
6. `Pendientes` y `Decisiones nuevas`: llévalos a Estado y a la tabla D.
7. Actualiza `Último avance`, `Siguiente paso exacto` y `Cola`. Reentrega solo los archivos tocados, con edición puntual.
Si un CIERRE contradice el plan de forma que cambia el alcance, no lo absorbas: señálalo y pide decisión.
