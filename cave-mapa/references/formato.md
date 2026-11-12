# Formato del bloque CONTEXTO VERIFICADO

Este bloque es la fuente del formato. `cave-planificacion` lo pega tal cual en `## 2. Contexto verificado` de `PLAN_APROBADO.md` (o en el microplan si no hay plan global). No renombres ni agregues campos.

Marcas: `[conf: <archivo>]` = confirmado con evidencia | `[por verificar]` = sin evidencia suficiente. Cada dato lleva una.

```
CONTEXTO VERIFICADO - <proyecto>
Fecha:
Skill: cave-mapa v<versión> | Alcance: completo | <área>
Stack: lenguaje y runtime vX [marca] | framework vX [marca] | BD/ORM [marca] | gestor de paquetes [marca]
Estructura: carpeta -> responsabilidad (máx 8 líneas)
Entradas: puntos de entrada y rutas principales [marca]
Comandos (gestor real):
- instalar: ... [marca]
- correr: ... [marca]
- build: ... [marca]
- prueba completa: ... [marca]
- prueba focal: ... [marca]
- lint y tipos: ... [marca]
- el CI corre: ... | no hay CI
Receta de verificación (entorno de trabajo): pasos en orden | estado: probada | por verificar
Variables de entorno (solo nombres): ... | ninguna
Convenciones: nombres, módulos, errores, estilo (máx 5 líneas) [marca]
Pruebas existentes: framework | carpeta | modelo: <ruta>
Documentación: README sí/no | DOCUMENTACION.md sí/no | otras: ...
Git: rama | árbol limpio | sucio (qué) | último tag | sin Git
Notas de riesgo: ninguna | - ...
Por verificar: ninguno | - dato: cómo comprobarlo
```

## Reglas
- Máximo ~60 líneas. Si no cabe, enfoca por área y dilo en `Alcance`.
- Comandos exactos, con el gestor real (no `npm` si el lockfile es de `pnpm`).
- Nada de valores de `.env`, claves ni datos personales.
- Un dato dudoso va en `Por verificar` con el comando de solo lectura que lo resuelve.
- `Notas de riesgo` describe, no resuelve.
