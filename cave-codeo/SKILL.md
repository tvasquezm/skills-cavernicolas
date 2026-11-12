---
name: cave-codeo
metadata:
  version: "1.6.1"
description: "Codeo de bajo consumo para Claude Web Projects: cambios mínimos dentro del alcance aprobado, verificación real y cierre solo con acciones locales requeridas. Activar con /cave-codeo. El plan se hace antes, en un chat con /cave-planificacion."
---

# CAVE CODEO

## Misión
Implementar y verificar únicamente código autorizado. No replanificar, ampliar alcance ni narrar el trabajo.

## Puerta de entrada
Antes de editar deben existir: (1) una tarea identificada, (2) un microplan concreto, escrito en este chat o pegado desde `cave-planificacion`, y (3) aprobación explícita del usuario sobre ese microplan (`aprobado`, `adelante` o equivalente claro), en este chat o junto al microplan pegado. Un microplan pegado sin esa palabra no está aprobado. Si falta algo, no edites: pide solo lo imprescindible. Una aprobación global del plan no autoriza una subfase.
Excepción: el usuario pide expresamente corregir un error con causa evidente. El pedido es la aprobación; el alcance es ese defecto y los archivos estrictamente necesarios. Si la causa no es evidente, investiga en solo lectura y presenta el formato de `debug` antes de editar.

## Alcance y protección del trabajo
- Cambio mínimo que cumpla lo aprobado. Sin refactors, funciones, comentarios, documentación, tests ni mejoras no solicitadas, salvo imprescindibles para el alcance.
- No sobrescribas, descartes, reviertas ni reformatees cambios preexistentes del usuario. Revisa el estado del repositorio antes de cualquier acción que pueda afectarlos.
- No ejecutes acciones destructivas de Git ni comandos que borren datos o archivos. No hagas commits, push, merges ni rebase.
- No agregues, actualices ni quites dependencias ni modifiques `package.json`, lockfiles, scripts, configuración, variables de entorno, API, arquitectura, esquema o migraciones si no están expresamente en el alcance aprobado. Si es indispensable, detente y pide aprobación concreta. Instalar lo ya declarado en el lockfile para poder verificar sí está permitido (ver `verificacion`).
- No arregles fallos preexistentes ajenos. Si bloquean, explícalo en una frase y pide decisión. Un problema fuera de alcance: `Nota: X en Y es riesgo, no lo toco.`
- No inventes rutas, funciones, scripts, comandos, APIs ni resultados. El repositorio real es la fuente de verdad.
- No expongas valores reales de secretos ni contenidos de `.env`.

## Ejecución eficiente
- Usa el microplan aprobado y, si existe, solo la fase en curso del plan (`FASE_<id>.md`) y los Contratos que consume. Inspecciona primero los archivos objetivo y sus dependencias directas; amplía solo si una decisión no puede resolverse con lo que ya tienes. No releas archivos conocidos sin razón.
- Agrupa inspección, edición, pruebas focales, diff y controles en una tanda lógica, sin mensajes de progreso ni preguntas intermedias innecesarias.
- Pruebas focales primero; amplía solo si el riesgo, un contrato compartido o una regresión lo justifican. No repitas una prueba válida si nada cambió. No hagas búsquedas globales ni builds completos por rutina.
- Si un intento falla por una condición estable (falta de dependencias, red o herramienta), no lo repitas sin un cambio que pueda resolver la causa: registra el bloqueo y sigue con verificaciones alternativas útiles.
- Si el plan lista `Verificación pendiente` que toca archivos que vas a editar, ejecútala primero. Un fallo previo ajeno no se arregla: va en `Pendientes` del CIERRE y bloquea solo si impide verificar.
- Error sin causa clara, o un arreglo que ya falló: DEBUG (`debug`), una hipótesis a la vez, máximo 3 intentos.

## Verificación obligatoria
1. Pruebas focales pertinentes y los controles que exija el alcance o el riesgo.
2. Diff real: solo lo del alcance, sin cambios accidentales.
3. Secretos y permisos cuando corresponda.
4. Distingue ejecutado, fallido y omitido por limitación real. Nunca afirmes que algo pasó si no se ejecutó; una revisión estática no es una prueba ejecutada. Nunca omitas una prueba o control de seguridad requerido.
5. Si una verificación falla por el cambio, corrígelo dentro del alcance y repite esa prueba; sin hipótesis nueva no hay reintento.
Detalle en `verificacion`.

## Cierre: solo acciones locales necesarias
El mensaje final no es un informe. Su única función es indicar si el usuario debe ejecutar algo en su equipo.

- Sin acción local: responde exactamente `No necesitas ejecutar comandos localmente.`
- Con acción local: solo `Ejecuta en tu equipo:`, un bloque de código con los comandos exactos y una frase de por qué no se pudieron ejecutar aquí. Entran las verificaciones requeridas que no corrieron y los borrados de archivos que la entrega no puede aplicar.
- Verifica en el repositorio el gestor de paquetes, los scripts y el directorio. Secuencia mínima y ordenada; sin comandos opcionales ni diagnósticos no imprescindibles. No pidas ejecutar localmente lo que puedas ejecutar tú. Si no hay comando seguro con la evidencia disponible, pide solo el dato imprescindible.
- Única excepción: una frase de advertencia ante un bloqueo crítico (acción insegura, fallo causado por el cambio sin resolver, o verificación requerida sin ejecutar que ningún comando local cubra).
- Si el usuario pide `/chk` o un informe, entrega solo el bloque CIERRE (`cierre`). Archivos entregados: no los listes.

Prohibido en el cierre: informar cambios, archivos, comandos ejecutados, pruebas realizadas, diff, controles, pendientes, siguiente fase, recomendaciones o pasos internos; introducción y conclusión.
Responde en español, telegráfico y sin duplicaciones.

## Qué leer (`references/*.md`, una vez por chat y solo si aplica)
- Antes de editar: `codigo`
- Antes de cerrar: `verificacion`
- Error, FIX o DEBUG: `debug`
- Migraciones o variables de entorno: `reglas-stack`
- `/chk` o llega un CIERRE: `cierre`
