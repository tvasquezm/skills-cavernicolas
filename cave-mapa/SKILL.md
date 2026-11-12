---
name: cave-mapa
metadata:
  version: "1.0.0"
description: "Mapa de proyecto de solo lectura para Claude Web Projects: explora un proyecto y entrega el bloque CONTEXTO VERIFICADO (stack, estructura, comandos reales para correr y probar, receta de verificación, convenciones) listo para pegar en el plan de /cave-planificacion. No edita nada. Activar con /cave-mapa. Va antes de /cave-planificacion, al empezar con un proyecto nuevo o desconocido."
---

# CAVE MAPA

## Misión
Explorar un proyecto y entregar su **Contexto verificado**: lo que `cave-planificacion` necesita para planear sin adivinar. No planificar, corregir ni opinar sobre el diseño.

## Puerta de entrada
Solo lectura: no requiere aprobación. Necesita (1) el proyecto accesible (repositorio, carpeta o zip) y, opcional, (2) el área o la tarea que se va a planificar, para enfocar. Sin proyecto accesible: pídelo y detente. Alcance por defecto `completo` (panorama breve); con área indicada, solo esa y sus dependencias directas.

## Límites duros
- No crear, editar ni borrar archivos del proyecto. El bloque se entrega en el chat.
- No ejecutar comandos que modifiquen archivos, dependencias, base de datos, Git o entorno. No instalar ni correr suites por defecto (ver `probar`).
- No ejecutar el código del proyecto contra red, servicios reales ni datos de producción.
- No exponer valores de `.env` ni secretos: solo los **nombres** de las variables.
- No inventar rutas, scripts, comandos ni versiones. Cada dato es `confirmado` (con su archivo) o `por verificar`. Sin `supuesto`: lo que no se confirma, se marca `por verificar`.
- No recomendar arquitectura, refactors ni arreglos. Un riesgo visto va en `Notas de riesgo`, en una línea.
- No ampliar el alcance ni auditar seguridad: eso es `cave-seguridad`.

## `probar` (opcional)
Solo si el usuario escribe `probar`: instalación congelada desde el lockfile y ejecución de los comandos de build y prueba ya declarados, sin tocar manifiestos ni lockfiles, y sin entregar artefactos generados. Un comando que funciona pasa a `probada`; uno que falla se registra con su error, sin arreglarlo. Sin red o herramienta: `por verificar` y comando local.

## Flujo
1. Inventario de la raíz y estado de Git (`exploracion`).
2. Stack y versiones, desde manifiestos y lockfiles.
3. Comandos reales: instalar, correr, build, pruebas (completa y focal), lint y tipos. Lo que corre el CI manda.
4. Estructura, entradas y convenciones, tomadas de 1 o 2 archivos modelo, no de todo el árbol.
5. Receta de verificación en el entorno de trabajo y variables necesarias (solo nombres).
6. Documentación existente, incluido `DOCUMENTACION.md` si existe.
7. Bloque `CONTEXTO VERIFICADO` (`formato`).

## Ejecución eficiente
Manifiestos y config primero; el código solo para fijar convenciones y entradas. Una tanda de inspección, sin mensajes de progreso. No releas lo conocido. Si el árbol es grande, enfoca por el área pedida y dilo en `Alcance`.

## Cierre
Solo el bloque en un bloque de código y una línea: `Pega este bloque en "2. Contexto verificado" de /cave-planificacion.` Si falta un dato que solo se obtiene en el equipo del usuario: antes, `Ejecuta en tu equipo:` con comandos de solo lectura exactos. Sin introducción, conclusión ni recomendaciones. Español, telegráfico.

## Qué leer (`references/*.md`, una vez por chat y solo si aplica)
- Antes de explorar: `exploracion`
- Antes de entregar: `formato`
