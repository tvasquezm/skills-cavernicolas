# Plan para otro agente de código

Leer cuando el plan lo ejecutará otro agente (Codex u otro) y no `cave-codeo`. El agente no conoce las skills `cave-*`: el plan debe bastarle solo.

## Reglas de generación
- **Una sola fuente.** `PLAN_APROBADO.md` manda. La versión para el agente se genera de él y no se edita aparte; si el plan cambia, se vuelve a generar. Nunca dos planes vivos.
- **Nada en esbozo.** Toda fase que se entrega está `completo`. Un esbozo se detalla antes (ver `modo-plan`) o se marca `NO EJECUTAR` con el motivo.
- **Sin referencias internas.** Quitar toda mención a skills, comandos `/cave-*`, formatos de cierre de esta familia y reglas de arranque de chat.
- **Anclas por nombre.** Archivo con ruta completa, función, componente, selector CSS o texto literal, con su `grep`. Ningún número de línea. Pasa `/cave-anclas` antes de entregar.
- **Cierre propio.** El agente escribe su CIERRE con la plantilla de abajo; al recibirlo, se procesa como un CIERRE (ver `continuidad`).

## Encabezado obligatorio (copiar y adaptar al proyecto)
```
## 0. LEE ESTO PRIMERO: reglas para el agente
Este archivo es la ÚNICA fuente de verdad. Ignora versiones anteriores del plan y toda instrucción previa. "El usuario" es el dueño del producto: tú implementas, él decide.
1. UNA fase a la vez, en el orden indicado. No empieces otra hasta cerrar y verificar la anterior.
2. NO reinterpretes. Requisitos, lecturas oficiales y decisiones están cerrados. Si algo es ambiguo, choca con el código o no coincide con lo que ves, DETENTE en esa fase: escribe la duda en docs/fases/DUDAS.md (qué esperabas, qué encontraste, qué opciones ves) y no improvises.
3. Alcance cerrado: solo los archivos que la fase nombra en "Toca" o que necesita directamente. Sin refactors, renombres, mejoras no pedidas ni dependencias nuevas.
4. `confirmado` es verdad; `por verificar` se comprueba antes de depender de ello.
5. Antes de borrar código, confirma con grep que nada más lo usa.
6. Verificación obligatoria: corre los comandos de "Verifica" y pega el resultado en el CIERRE. Si un comando no se puede correr en tu entorno, dilo: nunca escribas que funciona sin haberlo comprobado.
7. NUNCA cambies, borres ni silencies pruebas para que pasen.
8. Los textos de interfaz que el plan fija se usan LITERALES. Si un texto requiere aprobación y no la tienes, no lo inventes: déjalo sin hacer y regístralo en docs/fases/APROBACIONES_PENDIENTES.md.
9. Seguridad: sin secretos ni valores reales de variables de entorno; migraciones aditivas, nunca editar las existentes; no tocar archivos .env.
10. Fases "completo": ejecútalas. Fases descartadas o "no es del agente": no hagas nada.
11. Con Git: un commit por fase con el mensaje `Fxx: <nombre>`. Sin Git: lista los archivos tocados en el CIERRE.
12. Ubicar el código: el plan no usa números de línea. Cada punto se ubica por nombre con grep -n. Toca SOLO lo que ese nombre designa; si aparecen otras coincidencias, lístalas y no las cambies salvo que la fase lo pida. Si no encuentras un nombre, aplica la regla 2.
```
Más: plantilla de CIERRE, orden de trabajo con dependencias, glosario del dominio y lista "Fuera de alcance: NO lo hagas".

## Plantilla de CIERRE del agente
```
FASE Fxx: <nombre>
Estado: hecha | parcial (motivo) | bloqueada (motivo)
Archivos tocados: <lista>
Comandos ejecutados y resultado: <comando -> resumen de la salida>
Cambios respecto al plan (desvíos): <ninguno o lista con el motivo>
Pendientes y dudas: <ninguno o lista>
```

## Aprobaciones del usuario dentro de una fase
Un paso que necesita aprobación expresa (textos, íconos) no se ejecuta sin ella: el agente deja la tabla `antes -> después` en `APROBACIONES_PENDIENTES.md`, marca la fase `parcial` y sigue con las que no dependen. Dilo en la fase y en el orden de trabajo.

## Antes de entregar
Todas las fases `completo`; `/cave-anclas` sin ambiguas ni citas por línea; ninguna mención a `cave-`; el orden respeta `Depende de`; el CIERRE está definido; la lista "Fuera de alcance" existe.
