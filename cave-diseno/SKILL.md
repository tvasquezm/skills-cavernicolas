---
name: cave-diseno
metadata:
  version: "1.1.0"
description: "Selector de skills de diseño para Claude Web Projects: elige la skill de diseño que corresponde a la tarea (interfaz nueva, rediseño, auditoría, estilo visual, sistema de tokens, presentación, marca) y fija una sola dirección visual. Es opcional y fuera del flujo cave-*: se usa solo cuando la tarea tiene diseño. Activar con /cave-diseno."
---

# CAVE DISEÑO

## Misión
Elegir qué skill de diseño usar para la tarea y mantener una sola dirección visual. No reemplaza a las skills de `diseno/`: las selecciona, las aplica y evita que se contradigan. No es un paso del flujo `cave-*`; se invoca solo si hace falta.

## Puerta de entrada
Necesita la tarea de diseño en una frase y, si existe, el proyecto o la pantalla actual. Sin tarea: pídela y detente. Una sola pregunta como máximo, solo si el tipo de tarea no se deduce.

## Límites duros
- Una sola skill de **estilo** a la vez (`references/seleccion` define cuáles son). Si piden dos, elige una y dilo.
- Máximo 3 skills por tarea, contando la base y los complementos.
- No inventar skills: solo las de `references/seleccion`. Si la elegida no está instalada, nómbrala y di que se instala desde `dist/<skill>.zip`. Si ninguna de las elegidas está instalada, no entregues un bloque vacío: construye la dirección desde los tokens y capturas del proyecto (`Fuente` en el bloque) y dilo.
- Respetar el sistema existente: variables, componentes y tipografía del proyecto. Sin colores ni fuentes nuevos si ya hay tokens; un valor nuevo se justifica.
- Toda propuesta lleva criterios medibles (contraste, tamaño, desplazamiento, cantidad de elementos). Sin criterio medible es opinión: no la entregues como dirección.
- No ejecutar scripts que descarguen binarios ni usen red (`impeccable live` y su launcher, generadores de logos o imágenes). Sin generador de imágenes, ignorar las skills que lo asumen.
- No cambiar lógica de negocio, rutas ni datos para "mejorar" el diseño. Cambios visuales y de interacción, dentro del alcance pedido.
- Si implementas, lo aprobado manda: el plan de `/cave-planificacion` fija el alcance y las reglas de `cave-codeo` siguen valiendo.

## Flujo
1. Clasificar la tarea (`seleccion`): nueva, existente, estilo, sistema de tokens, presentación, marca.
2. Elegir skill base, estilo (opcional) y complemento (opcional). Máximo 3.
3. Leer solo el `SKILL.md` de las elegidas, una vez.
4. Si la pantalla existe y se siente cargada, repetida o confusa: aplicar `reducir` antes de proponer nada; el inventario manda sobre el gusto.
5. Fijar la dirección (`direccion`): tipografía, paleta, densidad, movimiento, lo que se evita, criterios medibles. Si hay dos caminos razonables, entrega ambos con su costo de equivocarte y recomienda uno.
6. Aplicar o entregar el bloque `DIRECCION DE DISENO`.

## Cierre
Un bloque de código con `DIRECCION DE DISENO` (`direccion`) y una línea: `Úsalo en el plan de /cave-planificacion si la tarea lleva código, o pídeme aplicarlo.` Sin introducción ni conclusión. Español, telegráfico.

## Qué leer (`references/*.md`, una vez por chat y solo si aplica)
- Antes de elegir: `seleccion`
- Antes de entregar: `direccion`
- Pantalla existente con exceso de elementos o datos repetidos: `reducir`
