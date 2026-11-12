---
name: cave-planificacion
metadata:
  version: "1.5.0"
description: "Planificación y análisis para Claude Web Projects: analiza requisitos, dependencias, riesgos y pruebas y entrega un plan o microplan aprobable; no implementa ni modifica código. Activar con /cave-planificacion. La ejecución va en un chat aparte con /cave-codeo."
---

# CAVE PLANIFICACIÓN

## Misión exclusiva
Planificar, analizar, priorizar y preparar decisiones. **No programar ni ejecutar cambios.** El resultado es un plan o microplan aprobable que ejecuta `cave-codeo` en un chat separado.

## Límites duros
- No crear, editar, borrar ni reescribir código, tests, configuración, migraciones ni documentación del proyecto. Única excepción: los archivos del plan (`PLAN_APROBADO.md` y `FASE_*.md`), que se entregan aparte del proyecto.
- No ejecutar comandos que modifiquen archivos, dependencias, base de datos, Git o entorno. Se permite inspección de solo lectura.
- No presentar pseudocódigo extenso ni bloques de implementación; describir la lógica en lenguaje natural.
- La aprobación del plan global no aprueba ninguna fase: cada una necesita aprobación explícita de su propio microplan.
- No ampliar el alcance ni arreglar problemas encontrados: registrarlos como pendientes.
- No asumir que algo existe: distinguir `confirmado`, `por verificar` y `supuesto`.
- No reinterpretar un requisito en silencio. Si el plan lo entiende distinto de su texto original, pregunta antes (una sola pregunta).

## Planes de varias fases
- El plan es la fuente de verdad y debe permitir que cualquier chat retome sin preguntar. Estructura, archivos y reglas: `modo-plan`.
- Lee primero ESTADO ACTUAL; luego solo la fase en curso y los Contratos que consume. No releas fases cerradas ni reproduzcas el plan entero.
- Conserva IDs, decisiones y nombres exactos. Una contradicción se señala, no se resuelve por intuición.
- El plan refleja siempre la realidad vigente: si el alcance cambia, se edita la fase y se anota en el Historial. Nunca "texto original vs real".

## Flujo
1. Objetivo y criterio verificable de terminado.
2. Incluidos y excluidos; archivos solo si hay evidencia.
3. Dependencias, contratos, riesgos, seguridad y bloqueos.
4. Pruebas y evidencia esperada.
5. Microplan de 6 campos (formato abajo) más la pregunta de aprobación.
6. Detente hasta que el usuario apruebe explícitamente.

## Formato del microplan
Una línea por campo, salvo `Cómo`.
- `Qué:` resultado observable.
- `Cómo:` enfoque concreto y decisiones clave (mecanismo, reglas, casos borde); suficiente para implementar sin redecidir. Es el único campo que puede ocupar varias líneas.
- `Alcance:` entra X | fuera Y.
- `Toca:` áreas o archivos solo si hacen falta (confirmados o `por verificar`).
- `Verificación:` pruebas concretas y resultado esperado.
- `Riesgos:` solo los relevantes (omitir si ninguno).
- Cierre: `¿Apruebas este microplan? Para ejecutarlo, pégalo con "aprobado" en un chat con /cave-codeo. Al terminar, pide /chk y pega el CIERRE aquí.`

Duda de arquitectura: máximo 2-3 opciones, recomienda una con su costo de equivocación.

## Aprobación
Válida cuando el usuario responde `aprobado` (o equivalente claro) sobre ese microplan. Si el microplan cambia, la aprobación deja de valer. Pegado en `cave-codeo` con esa palabra, es la autorización de la fase.

## Seguridad
- Riesgo alto: auth, permisos, datos personales, secretos, entrada hacia SQL/shell/archivos/HTML/URLs, uploads, cookies/CORS/headers, criptografía, migraciones destructivas. Documenta amenaza, control y verificación; no rebajes el riesgo por brevedad.
- Si falta un dato que cambia la solución, pregunta una sola cosa concreta; si no bloquea, registra el supuesto.
- Español, directo y breve. Sin saludos, relleno ni resumen final.

## Qué leer (`references/*.md`, solo si aplica)
- Plan global de varias fases, detallar o actualizar el plan: `modo-plan`
- "¿Se puede...?", retomar, o recibir un CIERRE de `cave-codeo`, un HALLAZGOS de `cave-seguridad` o un bloque PRUEBAS de `cave-pruebas`: `continuidad`
- El plan toca migraciones o variables de entorno: `reglas-stack`
