# Documento de revisión del equipo

Leer cuando el usuario pide que otras personas (no técnicas) revisen los cambios antes de ejecutarlos, o al recibir sus comentarios.

## Cuándo
Antes de pasar el plan a ejecución, si hay cambios visibles para las personas que usan el producto o decisiones que otros deben confirmar. Es una salida estándar del plan, no un extra.

## Formato
Un documento en lenguaje simple, sin jerga (sin nombres de archivos, fases ni código). Si hay herramienta de documentos compartibles, úsala; si no, un `md`. Secciones:
- **Cómo revisar:** 3 líneas. Cada punto lleva una línea de revisión con tres casillas: De acuerdo, Cambiar, Duda, y un comentario.
- **A. Lo que verán las personas** (cambios visibles).
- **B. Cambios por dentro** (seguridad, mantenimiento), cada uno explicado en una o dos frases.
- **C. Lo que NO se hará:** para que nadie espere algo que quedó fuera.
- **D. Decisiones ya tomadas** que conviene confirmar, cada una enlazada al punto que afecta.
- **E. Preguntas abiertas,** con una recomendación cuando la haya.
- **F. Textos nuevos** que verá el usuario, literales, para aprobar o corregir.
- **G. Qué viene después:** revisión, ajuste del plan, ejecución por fases.

## Cada punto
`Qué cambia` (comportamiento visible, hoy y después) | `Por qué` (la fuente: prueba, pedido del equipo o auditoría) | `Revisión`. Máximo 5 líneas. Un punto por cambio; no agrupes cambios que alguien podría aceptar por separado.

## Reglas
- Todo lo que se hará aparece, no solo lo dudoso. El revisor no debe tener que adivinar qué falta.
- Marca con `Ojo` lo que contradice a una persona que probó el producto o a otra decisión.
- Un texto técnico que no se pueda decir simple se explica con un ejemplo de pantalla.
- No incluyas fases, IDs de requisito ni decisiones internas (`R..`, `D..`, `F..`): llevan a confusión.
- Longitud: cabe en una lectura de 15 minutos (unas 3000 palabras como tope).

## Al recibir comentarios
1. Asigna cada comentario al punto que afecta. Los que no se entienden: una sola pregunta, con opciones y una recomendación.
2. Cambios pedidos: edita el plan (el requisito y la fase) y el documento; registra en Historial qué cambió y quién lo pidió.
3. Un punto sin comentarios se considera aceptado; dilo en el resumen.
4. Si un comentario pide algo que cambia permisos, datos o seguridad, no lo absorbas: señálalo como riesgo alto y planifícalo aparte.
5. Regenera el plan para otro agente si existe (ver `para-agente`).
