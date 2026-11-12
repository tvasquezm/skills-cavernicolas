# `DOCUMENTACION.md`: el archivo principal

Un solo archivo en la raíz del repositorio que dice cómo se documenta todo el proyecto. Es liviano (~120 líneas máximo) porque se lee en cada `sync`. Fuente única del formato.

## Inventario previo (solo lectura)
`README`, `docs/`, `CONTRIBUTING`, `ADR`/`decisions/`, `CHANGELOG`, OpenAPI/Swagger, `.env.example`, Storybook, docstrings (convención), documentación autogenerada (generador y comando), enlaces a wiki externa. Tipo de proyecto (app, API, librería, CLI, monorepo), audiencias reales y qué preguntas se repiten.

## Qué documentar (criterio)
Solo lo que una audiencia concreta necesita y se desactualiza si nadie lo cuida. Mínimo habitual: README (qué es y cómo arrancar), configuración y variables, y según el tipo: referencia de API, arquitectura, guía de contribución, operación. No crear documentos por completitud.

## Formato
```
# DOCUMENTACIÓN: <proyecto>
Skill: cave-docs v<versión> | Actualizado: <fecha>
Documento: borrador | aprobado | actualizado <fecha>

## 1. Propósito y audiencias
Para qué sirve esta documentación | quién lee qué (usuario, desarrollador, operador, contribuidor).

## 2. Mapa de documentos
ID | Documento | Ruta | Audiencia | Contiene | Fuente de verdad | Estado
DC1 | ... | README.md | desarrollador | qué es, cómo arrancar | package.json, scripts | vigente
(Estado: vigente | por crear | obsoleto | autogenerado: <comando>)

## 3. Reglas de actualización
Cambio -> documentos a revisar.
- Comando, script o requisito de entorno nuevo o cambiado -> DC..
- Variable de entorno nueva -> DC..
- Endpoint, contrato o formato visible -> DC..
- Esquema o migración -> DC..
- Dependencia mayor o versión de runtime -> DC..
- Decisión de arquitectura -> DC.. (ADR)

## 4. Convenciones
Idioma | formato (Markdown) | nombres de archivo | títulos | plantilla por tipo | ejemplos ejecutables y verificados | enlaces relativos | diagramas | fechas | tono y longitud.

## 5. Fuera de este mapa
CHANGELOG y versiones (`cave-release`) | plan y fases (`cave-planificacion`, fuera del repo) | secretos y valores de entorno | comentarios y docstrings (código).

## 6. Verificación
Qué se comprueba tras editar y con qué comando real: comandos del README, enlaces, ejemplos, versiones citadas. Lo que no se pueda correr aquí va en `Ejecuta en tu equipo:`.

## 7. Historial
Fecha | qué cambió | por qué | quién lo aprobó
```

## Reglas
- IDs `DC<n>` estables (no `D<n>`, que son decisiones del plan). No se reutilizan ni se renombran.
- Una fuente de verdad por documento: de dónde se sacan los hechos (manifiesto, código, esquema). Si la fuente cambia, el documento se revisa.
- `README` enlaza a `DOCUMENTACION.md` con una sola línea. Es la única edición ajena que hace `init`.
- Estado y fechas se actualizan con edición puntual, sin regenerar el archivo.
- Un cambio de convención es un cambio de alcance: se edita el mapa, se anota en `Historial` y se pide aprobación.
