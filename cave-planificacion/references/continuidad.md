# SPIKE, retomar y bloques recibidos

Leer ante "¿se puede...?", al retomar, o al recibir un CIERRE de `cave-codeo`, un HALLAZGOS de `cave-seguridad`, un bloque PRUEBAS de `cave-pruebas`, un CONTEXTO VERIFICADO de `cave-mapa`, un DEPS de `cave-deps` o un DOCS de `cave-docs`.

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

## Al recibir HALLAZGOS (`cave-seguridad`)
Formato recibido: `S-<n> | severidad | título | archivos | corrección | verificación`. Es entrada para planificar: no se corrige aquí.
1. Conserva los IDs `S-<n>` y la severidad tal cual; no la rebajes por brevedad ni la subas por alarma. Sin plan global, regístralos como requisitos de origen (`R`, fuente `cave-seguridad S-<n>`); con plan, agrégalos a `3. Requisitos de origen`.
2. Ordena por severidad: CRÍTICO y ALTO primero. Agrupa por causa raíz o por archivos comunes; cada microplan respeta el tope de una fase (~10 archivos o ~500 líneas de diff).
3. Cada microplan lleva riesgo ALTO si toca auth, permisos, datos personales, secretos o entrada hacia SQL/shell/archivos/HTML/URLs: amenaza, control y verificación. La `Verificación` es el caso negativo que el hallazgo declara.
4. Secreto expuesto: el plan incluye, aparte del código, la rotación de la credencial y la revisión de su uso. Es una acción manual del usuario; no la ejecuta `cave-codeo`. Sin valores de secretos en el plan.
5. Un hallazgo `por verificar` no se corrige a ciegas: el primer paso del microplan es confirmarlo en solo lectura.
6. Tras ejecutar las correcciones, el cierre del flujo es una reauditoría con `/cave-seguridad`. Un hallazgo no se da por resuelto sin ella.
Termina con el microplan del primer grupo y su pregunta de aprobación.

## Al recibir PRUEBAS (`cave-pruebas`)
Formato recibido: bloque `PRUEBAS - <proyecto>` (Alcance, Archivos de prueba, Casos, Verificación, Fallan por la razón correcta, Hallazgos de código, Pendientes).
1. `Verificación` con algo `omitida` o `fallida`: el trabajo queda `ejecutado, por verificar` y el comando pasa a `Verificación pendiente` del Estado, igual que con un CIERRE.
2. `Hallazgos de código` son fallos reales del código, no corregidos. Cada uno pasa a pendiente o a microplan de arreglo para `cave-codeo`, con el comando que lo reproduce como verificación. No lo absorbas en el alcance de la fase actual.
3. `Fallan por la razón correcta: por verificar` se anota como verificación pendiente.
4. Los archivos de prueba nuevos se registran en el plan como entregados (en `Toca` o `Contratos`, solo si otra fase los consume). `Pendientes`, a Estado.
5. Actualiza `Último avance`, `Siguiente paso exacto` y `Cola`, con edición puntual.
Si el bloque contradice el plan de forma que cambia el alcance, no lo absorbas: señálalo y pide decisión.

## Al recibir CONTEXTO VERIFICADO (`cave-mapa`)
Formato recibido: bloque `CONTEXTO VERIFICADO - <proyecto>` (Stack, Estructura, Entradas, Comandos, Receta de verificación, Variables, Convenciones, Pruebas existentes, Documentación, Git, Notas de riesgo, Por verificar).
1. Pégalo tal cual en `## 2. Contexto verificado` de `PLAN_APROBADO.md` (o en el microplan si no hay plan global). Conserva las marcas `[conf: ...]` y `[por verificar]`.
2. Lo `confirmado` es verdad; lo `por verificar` se comprueba en solo lectura antes de que un microplan dependa de ello.
3. Si ya había contexto, fusiona con edición puntual: lo nuevo y confirmado manda. No dupliques.
4. `Notas de riesgo` y `Por verificar` pasan a pendientes del Estado; `Comandos` y `Receta` alimentan la `Verificación` de cada microplan.
5. Si `DOCUMENTACION.md` no existe y el proyecto lo necesita, regístralo como fase o pendiente (`/cave-docs init`), sin absorberlo en otra fase.

## Al recibir DEPS (`cave-deps`)
Formato recibido: bloque `DEPS - <proyecto>` (Motivo, Línea base, Actualizados, Sin actualizar, Verificación, Transitivas, Rupturas, Avisos, Reversión, Pendientes).
1. `Verificación` con algo `omitida` o `fallida`: queda `ejecutado, por verificar` y el comando pasa a `Verificación pendiente` del Estado.
2. `Rupturas` son cambios de código que la actualización exige y no se hicieron. Cada una pasa a microplan para `cave-codeo` (o a pendiente), con el comando que la reproduce como verificación. No la absorbas en otra fase.
3. `Sin actualizar` y `Pendientes` van a Estado. Un `major` aplazado es una decisión: regístrala en la tabla D.
4. Si el motivo era `S-<n>`, el cierre es `/cave-pruebas` y una reauditoría con `/cave-seguridad`; no se da por resuelto sin ella.
5. `Aprendido` sobre el entorno (versión de runtime, gestor) se promueve a `2. Contexto verificado`. Actualiza `Último avance`, `Siguiente paso exacto` y `Cola`, con edición puntual.

## Al recibir DOCS (`cave-docs`)
Formato recibido: bloque `DOCS - <proyecto>` (Modo, Índice, Documentos, Verificación, Desfases, Por verificar, Pendientes).
1. `Verificación` omitida o fallida: `ejecutado, por verificar`, igual que con un CIERRE.
2. `Desfases`: la doc dice una cosa y el código otra. Decide cuál es la correcta antes de planear: si el error está en el código, microplan para `cave-codeo`; si está en la doc, pendiente para `cave-docs sync`. No lo resuelvas por intuición.
3. Tras `init`, anota en `2. Contexto verificado`: `DOCUMENTACION.md existe` con su ruta. Los documentos `por crear` pasan a pendientes.
4. Una fase que cambia comandos, variables, contratos o esquema declara en `Verificación` o `Pendientes` el `sync` de documentación que le corresponde, según las reglas de `DOCUMENTACION.md`.
5. Actualiza `Último avance`, `Siguiente paso exacto` y `Cola`, con edición puntual.
