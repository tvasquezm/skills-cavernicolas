---
name: cave-docs
metadata:
  version: "1.0.0"
description: "Documentación para Claude Web Projects: crea el archivo principal DOCUMENTACION.md que define cómo se documenta todo el proyecto (mapa de documentos, reglas de actualización, convenciones) y luego crea o sincroniza README y demás docs tras cada cambio, verificando cada afirmación contra el repositorio. No toca código, CHANGELOG ni versiones. Activar con /cave-docs. Va tras /cave-seguridad y antes de /cave-release."
---

# CAVE DOCS

## Misión
Que la documentación diga lo que el proyecto hace hoy, bajo una sola convención. El archivo principal `DOCUMENTACION.md` es la regla: define qué se documenta, dónde, para quién y cuándo se actualiza. No programar ni replanificar.

## Modos
- `init`: crea `DOCUMENTACION.md` (y una línea en el README que apunte a él). Es lo primero en un proyecto.
- `sync`: tras un cambio, crea o actualiza los documentos afectados según `DOCUMENTACION.md`.
- `revisar`: solo lectura. Compara docs con código y entrega los desfases. No edita.
Sin `DOCUMENTACION.md`, `sync` no corre: se hace `init` primero (una frase y se detiene).

## Puerta de entrada
Antes de editar deben existir: (1) el modo, (2) un plan concreto escrito en este chat o pegado: en `init`, la propuesta del archivo principal; en `sync`, la lista de documentos a tocar y qué cambia en cada uno, derivada de `DOCUMENTACION.md` y del cambio real, y (3) aprobación explícita (`aprobado`, `adelante` o equivalente claro). Un plan pegado sin esa palabra no está aprobado. `revisar` no necesita aprobación.
Excepción: el usuario pide expresamente una doc concreta (`documenta X`). El pedido es la aprobación; el alcance es ese documento. Si no existe `DOCUMENTACION.md`, se avisa en una línea y se sigue.

## Límites duros
- Edita solo documentación: `DOCUMENTACION.md`, README, `docs/`, guías y los archivos que el mapa declare. **Nunca código, pruebas, configuración ni dependencias.** Comentarios y docstrings son código: van por microplan de `cave-codeo`.
- No toques `CHANGELOG`, versiones ni notas de release (`cave-release`), ni `PLAN_APROBADO.md` y `FASE_*.md` (`cave-planificacion`).
- Cada afirmación se verifica contra el repositorio: comandos leídos del manifiesto o ejecutados, rutas con `ls`, nombres con grep, variables de entorno con grep. Lo no verificable se omite o se marca `por verificar`. Nada de intención o futuro presentado como hecho.
- No expongas secretos ni valores de `.env`: solo nombres. No documentes en lugares públicos una vulnerabilidad sin corregir. Sin datos personales.
- No amplíes: no reescribas documentos no afectados, no reformatees en masa ni cambies el idioma o el tono ya establecidos. No borres documentos sin aprobación expresa; márcalos `obsoleto`.
- Documentos autogenerados (referencia de API, typedoc, etc.) no se editan a mano: se indica el comando que los regenera.
- No hagas commits, push ni merges. No pises cambios del usuario.

## Flujo `init`
1. Inventario de solo lectura (`documentacion-md`): docs existentes, tipo de proyecto, audiencias, convenciones visibles.
2. Propuesta: adoptar lo que existe, listar lo mínimo útil que falta (sin inflar) y fijar reglas de actualización y convenciones.
3. Entrega: crea `DOCUMENTACION.md` con `Documento: borrador`. En el chat, resumen de máximo 5 líneas y la pregunta de aprobación. Una sola pregunta si falta idioma o audiencia.
4. Al aprobar: `Documento: aprobado`, edición puntual. Los documentos `por crear` se escriben después con `sync`.

## Flujo `sync`
1. Lee `DOCUMENTACION.md` (mapa, reglas y convenciones) y el cambio: `git diff`, rango de commits o un CIERRE, PRUEBAS, DEPS o HALLAZGOS pegado.
2. Mapea cambio -> documentos afectados con las reglas de actualización. Si el cambio no encaja en ninguna, propón el ajuste al mapa en el mismo plan.
3. Plan por documento, detente hasta la aprobación.
4. Edita, verifica cada afirmación (`redaccion`), comprueba enlaces y ejemplos, y actualiza estado y fecha en la tabla del mapa.

## Flujo `revisar`
Compara cada documento del mapa con el código y entrega `Desfases` con evidencia (`doc:línea` vs `archivo:línea`), documentos faltantes del mapa y enlaces rotos. No edita.

## Cierre
No es un informe. Solo indica si el usuario debe ejecutar algo en su equipo.
- Sin acción local: `No necesitas ejecutar comandos localmente.`
- Con acción local: `Ejecuta en tu equipo:`, bloque con comandos exactos (p. ej. regenerar documentación autogenerada, comprobar enlaces) y una frase de por qué no corrieron aquí.
- `/chk` o un informe: solo el bloque DOCS (`cierre`).
Prohibido en el cierre: listar documentos o cambios, introducción y conclusión. Español, telegráfico.

## Qué leer (`references/*.md`, una vez por chat y solo si aplica)
- `init`: `documentacion-md`
- Antes de escribir o editar un documento: `redaccion`
- `/chk`: `cierre`
