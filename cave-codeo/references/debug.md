# FIX y DEBUG

Leer ante un error. Orden: error -> causa -> solución -> aprobación -> implementación -> verificación. La aprobación la da el microplan o el pedido explícito de corregir con causa evidente (`SKILL.md`).

## FIX (causa evidente)
```
Error: X
Causa: Y
Cambio: Z
```
Con pedido explícito de corregir: corrige directo y verifica síntoma antes y después. Sin ese pedido: presenta el bloque y espera aprobación. Causa no evidente: DEBUG.

## DEBUG (causa no clara, o un arreglo ya falló)
```
DEBUG
Síntoma: X (reproducido: sí/no)
Evidencia: qué se vio, por capa si hay varias
Hipótesis: UNA, con "porque"
Prueba mínima: un solo cambio o comando
Intentos fallidos: n/3
```
Investigar (leer, reproducir, ejecutar sin modificar) no requiere aprobación; editar sí.

## Protocolo
1. **Causa antes que arreglo.** Lee el error completo y literal (mensaje, stack, archivo, línea); si el usuario lo contó con sus palabras, pide el texto literal. Reproduce. Mira qué cambió (`git diff`, dependencias, config, entorno).
2. **Rastrea hacia atrás** hasta el origen del valor malo y arregla ahí, no donde explota. Compara con un caso que sí funciona y lista todas las diferencias.
3. **Una hipótesis con "porque"**, probada con el cambio más chico, una variable por vez. Si no era, deshaz el cambio de prueba editándolo de vuelta (sin comandos destructivos de Git ni tocar cambios previos del usuario) y formula otra; no apiles arreglos.
4. **Varias capas** (front -> API -> base; CI -> build): no arregles hasta saber en qué frontera se rompe. Pide la evidencia de todas las capas en un solo mensaje y investiga solo la capa donde el dato deja de ser correcto.
5. Si no lo sabes: `No entiendo X.` y pide el dato concreto. Nunca pidas ni imprimas el valor de una variable secreta; comprueba solo si está definida.

## Regla de 3
Al tercer arreglo fallido, para: no hay cuarto. Suele ser un problema de enfoque, no de detalle. Responde:
```
3 arreglos fallaron. Sospecho el enfoque, no el detalle: X.
Opciones: A - ... / B - ...
Recomiendo A. ¿Cuál?
```
Señales de que se está adivinando (volver al paso 1): "probemos a ver si anda", varios cambios a la vez, proponer una solución antes de rastrear el dato, "un intento más" tras dos fallos.

Ideas adaptadas de `systematic-debugging` de Superpowers (MIT, https://github.com/obra/superpowers), reescritas sin copiar texto.
