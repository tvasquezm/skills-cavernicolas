---
name: cave-anclas
metadata:
  version: "1.0.0"
description: "Verifica en solo lectura que las referencias de un plan al código (archivos, funciones, componentes, selectores CSS, variables) existan en el proyecto, y detecta citas por número de línea. Activar con /cave-anclas, antes de entregar un plan a otro agente de código o a /cave-codeo, y al retomar un plan con el código cambiado."
---

# CAVE ANCLAS

## Misión
Comprobar que cada nombre que un plan cita del código existe de verdad y apunta a un solo lugar. No corrige el plan ni el código: informa. Las correcciones las hace `cave-planificacion`.

## Límites duros
- Solo lectura. No editar el plan, el código ni la configuración. Sin red.
- El script no ejecuta nada del proyecto: solo lee archivos de texto.
- Un resultado no es un veredicto: `No encontradas` puede ser un error del plan, algo que la fase crea, o una afirmación negativa. Clasifica cada caso antes de reportarlo.

## Entrada
El plan (`.md`) y la carpeta raíz del proyecto. Sin alguno de los dos, pídelo y detente. Si el proyecto no está disponible, dilo: no verifiques de memoria.

## Flujo
1. Ejecutar: `python3 scripts/verificar_anclas.py <plan.md> <raíz del proyecto>` (`--json` para salida estructurada).
2. Revisar cada grupo del resultado:
   - `Verificadas`: no se listan.
   - `No encontradas`: ¿la fase la crea y falta decirlo? ¿está mal escrita? ¿se movió o se borró?
   - `Ausentes esperadas`: el plan afirma que no existe; confirmar que sigue siendo cierto.
   - `Ambiguas`: el nombre coincide con varios archivos; el plan debe citar la ruta completa.
   - `Citas por línea`: prohibidas; deben pasar a nombre (función, componente, selector o texto literal) con su `grep`.
   - `Nuevas`: las crea el plan; comprobar que la carpeta destino existe.
3. Entregar el bloque de cierre.

## Cierre
Un bloque de código y una línea:
```
ANCLAS - <plan> | <fecha>
Resumen: verificadas N | nuevas N | no encontradas N | ausentes esperadas N | ambiguas N | citas por línea N
Corregir en el plan:
- plan:<línea> | <ancla> | <problema> | <corrección propuesta>
Sin problemas: ninguno | grupo
```
`Para corregirlo, pásalo a /cave-planificacion.` Sin introducción ni conclusión. Español, telegráfico.

## Qué sabe y qué no el script
- Reconoce entre comillas invertidas: rutas de archivo, selectores CSS (`.clase`, `:root`) y nombres (camelCase, PascalCase, `NOMBRE_CONSTANTE`, `funcion()`).
- Ignora comandos, valores y texto libre. No valida textos de interfaz entre comillas ni que el nombre esté en el archivo correcto.
- Un nombre se da por encontrado si aparece en cualquier archivo de texto del proyecto: confirma el archivo concreto con `grep` cuando la ambigüedad importe.
