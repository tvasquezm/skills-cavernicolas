# Redacción y verificación

## Antes de escribir
Lee la convención (`DOCUMENTACION.md` sección 4), un documento existente como modelo de tono y estructura, y la fuente de verdad del documento. No escribas desde memoria ni desde el nombre de las cosas.

## Cada afirmación, con evidencia
- Comandos: léelos del manifiesto, `Makefile` o CI; si se pueden ejecutar aquí sin escribir en el proyecto, ejecútalos. Si no, `por verificar` y `Ejecuta en tu equipo:`.
- Rutas y nombres: `ls` y grep. Versiones: manifiesto o lockfile.
- Variables de entorno: grep de lecturas y `.env.example`; solo nombres, con para qué sirven y si son obligatorias.
- Comportamiento: léelo del código o de una prueba, no de otro documento.
- Contradicción entre doc y código: manda el código. Si el código parece el equivocado, no lo arregles: `Desfase` y pendiente para `cave-planificacion`.

## Plantillas mínimas por tipo
- **README:** qué es (1-2 líneas) | requisitos | instalar | correr | probar | estructura en pocas líneas | enlace a `DOCUMENTACION.md`.
- **Configuración y entorno:** variable | obligatoria | para qué | valor de ejemplo ficticio.
- **API o contratos:** ruta o función | entrada | salida | errores | ejemplo mínimo verificado.
- **Arquitectura:** diagrama simple (Mermaid) y responsabilidad por módulo; sin listar archivos uno por uno.
- **ADR:** contexto | decisión | alternativas descartadas | consecuencias.
- **Operación o runbook:** síntoma | causa probable | comando de comprobación | acción.
- **Contribución:** cómo preparar el entorno, convenciones y cómo probar.

## Estilo
Telegráfico y concreto. Una idea por párrafo. Ejemplos mínimos que funcionan, con datos ficticios. Sin marketing, sin relleno, sin "actualmente" ni fechas que caduquen salvo en `Historial`. Conserva el idioma y el tono del proyecto.

## Verificación al editar
1. Enlaces relativos y anclas existen.
2. Los ejemplos de código o comandos se leen contra la fuente real o se ejecutan.
3. Las versiones y los nombres citados coinciden con manifiesto y código.
4. Diff real: solo documentos del plan, sin reformateos ajenos ni archivos de código.
5. Sin secretos ni valores de `.env`.
6. Estado y fecha del documento actualizados en el mapa.
Lo no ejecutado es `OMITIDO` con motivo y comando local; nunca se afirma que algo funciona si no se comprobó.
