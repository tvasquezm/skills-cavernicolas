# Plan global: estructura y reglas

Leer al plantear un plan de varias fases, al detallar una fase o al actualizar el plan.

## Cuándo
Plan global solo si la tarea necesita varias fases o varios chats. Si una tarea de una fase revela varias piezas (interfaz compartida, dependencias, migraciones), decir `Esto creció: paso a plan global.` Nunca al revés. Aprobarlo no autoriza ejecutar ninguna fase.

## Principio
El plan es lo único que sobrevive entre chats. Junto con el código debe bastar para retomar donde se dejó, sin preguntar ni redecidir. Lleva el QUÉ y el CÓMO con el detalle crucial; archivos solo cuando son necesarios (el cambio vive en un lugar no obvio o hay riesgo de tocar el equivocado).

## Archivos
- `PLAN_APROBADO.md`: índice y estado. Es liviano porque se lee en cada chat.
- `FASE_<id>.md`: una por fase, con su plan y su CIERRE. Se lee solo la fase en curso y los Contratos de las que consume. Plan chico (hasta 3 fases): las fases van dentro de `PLAN_APROBADO.md`.
- **IDs estables:** `R1..` requisitos, `D1..` decisiones, `F<id>` fases. No se reutilizan ni se renombran; los microplans los citan en vez de repetir texto. El orden de ejecución vive en `Cola`, no en el ID.
- **Entrega:** se crean como archivos descargables con `Documento: borrador`. En el chat, solo un resumen de máximo 5 líneas (fases y decisiones abiertas) y la pregunta de aprobación. Al aprobar: `Documento: aprobado` con edición puntual, sin regenerar. Sin poder crear archivos: un bloque `md` por archivo. El usuario los sube al Project y reemplaza los anteriores. Van aparte del repo, sin valores de `.env` ni claves.

## PLAN_APROBADO.md
```
# PLAN: <proyecto> | <fecha>
Skill: cave-planificacion v<versión>

## ESTADO ACTUAL (leer primero)
Documento: borrador | aprobado | actualizado <fecha>
En curso: F<id> - nombre | estado: sin empezar | microplan aprobado | ejecutada, por verificar | cerrada
Último avance: qué quedó funcionando (1-2 líneas)
Siguiente paso exacto: ...
Cola: F.., F.., F.. (orden de ejecución)
Verificación pendiente: ninguna | - comando | fase | quién lo corre
Decisiones abiertas: ninguna | - D? ... (bloquea: sí/no)
Bloqueos: ninguno | ...
Pendientes fuera de alcance: ninguno | - ... (riesgo si aplica)

## CÓMO RETOMAR (para cualquier chat)
1. Lee ESTADO ACTUAL y solo la fase en curso; de las cerradas, solo los Contratos que consumes.
2. Lo `confirmado` es verdad; lo `por verificar` se comprueba antes de depender de ello.
3. No rehagas ni cuestiones decisiones registradas; si una choca con la realidad, anótala en Decisiones abiertas.
4. Cada fase se ejecuta solo con su microplan aprobado.

## 1. Propósito y alcance
Para qué se hace y qué valor da | resultado final observable | incluye | fuera | no aprobado.

## 2. Contexto verificado
Stack y versiones relevantes, qué existe hoy relacionado, convenciones a respetar. **Cómo se corre y se prueba** (comandos reales) y la **receta de verificación en el entorno de trabajo** (instalación, generación de clientes, variables) para que ninguna fase quede sin probar. Cada dato: `confirmado` o `por verificar`.

## 3. Requisitos de origen
R1 | texto original en una línea | fuente | fase
(Es la referencia contra la que se valida lo que se entiende. Sin esta tabla, un requisito mal leído nadie lo detecta.)

## 4. Decisiones transversales
D1 | decisión | descartado | por qué | costo si está mal

## 5. Mapa de fases
ID | nombre | depende de | entrega | detalle: completo|esbozo | estado

## 6. Seguridad, datos y entorno
Amenaza | control | verificación; env vars nuevas (solo nombres); migraciones. Omitir si no aplica.

## 7. Historial
Fecha | qué cambió | por qué | quién lo aprobó
```

## FASE_<id>.md
```
# FASE <id>: nombre
Estado: sin empezar | microplan aprobado | ejecutada, por verificar | cerrada
Detalle: completo | esbozo
Requisitos: R..
Depende de: F..
Entrega: sola | junto con F.. (por qué)

## PLAN
Qué: resultado observable al terminar (comportamiento, no archivos).
Cómo: enfoque concreto (ver abajo).
Decisiones: D.. | nuevas: elegido X sobre Y porque Z.
Contratos: Consume (exacto) | Produce (exacto)
Toca: áreas o módulos; rutas solo si son necesarias.
No hacer: límites de la fase.
Verifica: criterio -> comando y resultado esperado.
Riesgo y reversión: ...

## CIERRE (se llena al cerrar)
Fecha:
Hecho: qué quedó funcionando
Contratos reales: nombres, rutas, firmas y formatos exactos que quedaron
Desvíos del plan: ninguno | qué se hizo distinto y por qué
Decisiones nuevas: ninguna | decisión - por qué
Verificación: ejecutada: comando -> resultado | fallida: ... | omitida: motivo + comando local
Aprendido del entorno: nada | qué hizo falta para poder probar
Pendientes: ninguno | - A (incluye lo encontrado fuera de alcance)
```

## Cómo escribir cada fase
- **Qué:** lo que el usuario o el sistema podrá hacer o verá al terminar.
- **Cómo:** detalle suficiente para implementar sin volver a decidir: flujo paso a paso, reglas de negocio y validación, estructuras y contratos exactos, orden de operaciones, casos borde y errores, qué se reutiliza. Sin código ni pseudocódigo extenso.
- **Contratos:** nombres, firmas, rutas o formatos exactos, tomados del código o de un CIERRE, nunca de memoria. `Produce:` = `nombreExacto(params): tipo`.
- **Entrega:** si una fase deja el sistema inconsistente hasta que otra llegue (por ejemplo un backend que rechaza al frontend viejo), se declara aquí.
- **Esbozo:** solo Qué y Requisitos. Antes de su microplan, esta skill la detalla leyendo el código (solo lectura), completa y marca `completo`; si el detalle cambia alcance o tamaño, lo dice y pide aprobación. Una fase en esbozo no se ejecuta.

## Antes de entregar el plan
Cada requisito R tiene fase; cada fase `completo` tiene Qué, Cómo y Verifica; cada decisión tiene su porqué; lo que una fase consume coincide con lo que otra produce; ningún requisito está reinterpretado sin confirmar; la receta de verificación está probada o marcada `por verificar`; no hay archivos listados sin necesidad.

## Reglas
- Una fase cabe en un chat (~10 archivos o ~500 líneas de diff como tope). Si crece al ejecutar, se divide.
- Falta un dato que cambia el diseño: `Falta X.` y esperar; si se puede verificar en el código, verificarlo. Nunca un plan especulativo.
- Aprobación parcial: solo lo aprobado pasa a ejecución; el resto queda pendiente y no se vuelve a preguntar.
- Alcance que crece: va como pendiente o microplan nuevo, no se suma a lo aprobado. Un cambio de alcance se edita en la fase y se registra en el Historial en el mismo paso.
- Estado y notas no se acumulan como texto corrido: cada dato va en su campo (Estado, CIERRE, Historial).
