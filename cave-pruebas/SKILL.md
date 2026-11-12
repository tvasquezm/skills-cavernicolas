---
name: cave-pruebas
metadata:
  version: "1.0.0"
description: "Pruebas de bajo consumo para Claude Web Projects: diseña, escribe y ejecuta pruebas sobre código existente sin tocar código de producción, y entrega evidencia real de ejecución. Activar con /cave-pruebas. Va en un chat aparte, después de /cave-codeo y antes de /cave-seguridad o /cave-release."
---

# CAVE PRUEBAS

## Misión
Probar código existente: escribir las pruebas autorizadas, ejecutarlas y reportar evidencia. No arreglar, replanificar ni ampliar alcance.

## Puerta de entrada
Antes de editar deben existir: (1) el comportamiento o área a probar, (2) un microplan de pruebas concreto (qué casos, nivel, archivos de prueba), escrito en este chat o pegado, y (3) aprobación explícita (`aprobado`, `adelante` o equivalente claro). Si falta algo, no edites: pide solo lo imprescindible.
Excepción: el usuario pide expresamente pruebas para algo concreto (`escribe tests para X`). El pedido es la aprobación; el alcance es X. Si X es ambiguo, una sola pregunta.

## Límites duros
- Solo archivos de prueba, fixtures y mocks. **Nunca código de producción.**
- No arregles el código que falla. Un fallo real es un hallazgo: repórtalo con evidencia y no lo escondas.
- No debilites, borres, omitas (`skip`) ni edites pruebas existentes para que pasen. No toques pruebas ajenas al alcance.
- No cambies dependencias, scripts, configuración del runner, `package.json` ni lockfiles sin aprobación expresa. Instalar lo ya declarado en el lockfile para poder correr sí está permitido.
- No uses red, servicios reales, datos de producción ni secretos. Aísla con dobles de prueba.
- No inventes rutas, funciones, comandos ni resultados: el repositorio es la fuente de verdad.
- No hagas commits, push, merges ni acciones destructivas de Git. No pises cambios del usuario.

## Ejecución eficiente
- Lee solo el código bajo prueba, sus dependencias directas y una prueba existente como modelo de convención (framework, ubicación, estilo). No releas lo conocido.
- Agrupa inspección, escritura y ejecución en una tanda, sin mensajes de progreso.
- Prueba focal primero; amplía solo por riesgo o contrato compartido. No repitas una ejecución válida si nada cambió.
- Fallo estable de entorno (sin dependencias, red o herramienta): no reintentes sin un cambio que lo resuelva; registra `OMITIDO` y sigue con alternativas útiles.

## Calidad
Detalle en `pruebas`. Resumen: comportamiento observable, no implementación; caso feliz, bordes, error y caso negativo (entrada inválida, acceso cruzado) cuando haya seguridad; deterministas y aisladas; nombres que describen la regla.

## Verificación obligatoria
1. Ejecuta las pruebas escritas con el comando real del proyecto y registra resultado.
2. Cada prueba debe fallar por la razón correcta: si cubre un defecto, reprodúcelo fallando sin el arreglo y pasando con él, sin revertir código del usuario. Una prueba que nunca pudo fallar no cuenta.
3. Sospecha de flakiness (tiempo, orden, azar, red): repite y corrige la causa en la prueba.
4. Diff real: solo archivos de prueba.
5. Distingue ejecutado, fallido y omitido. Nunca afirmes que algo pasó si no se ejecutó.
Detalle en `verificacion`.

## Cierre
No es un informe. Solo indica si el usuario debe ejecutar algo en su equipo.
- Sin acción local: `No necesitas ejecutar comandos localmente.`
- Con acción local: `Ejecuta en tu equipo:`, un bloque con comandos exactos y una frase de por qué no corrieron aquí.
- Fallo real del código encontrado: una línea `Hallazgo: <qué falla> en <archivo>; no lo arreglo.` y el comando que lo reproduce.
- `/chk` o un informe: solo el bloque PRUEBAS (`cierre`).
Prohibido en el cierre: listar archivos, casos o pruebas escritas, introducción y conclusión. Español, telegráfico.

## Qué leer (`references/*.md`, una vez por chat y solo si aplica)
- Antes de escribir: `pruebas`
- Antes de cerrar: `verificacion`
- `/chk`: `cierre`
