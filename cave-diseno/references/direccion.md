# Formato del bloque DIRECCION DE DISENO

Una dirección visual por tarea. Si el usuario ya fijó una (por ejemplo en el proyecto), se respeta y no se reemplaza.

```
DIRECCION DE DISENO - <proyecto o pantalla>
Fecha:
Skill: cave-diseno v<versión>
Tarea: <una línea>
Fuente: skills | tokens y capturas del proyecto
Skills usadas: base <skill> | estilo <skill> | ninguno | complemento <skill> | ninguno
No instaladas: ninguna | - <skill>
Tipografía: títulos <fuente> | texto <fuente>
Paleta: fondo | texto | acento (valores o variables)
Densidad y layout: <una línea>
Alternativas: ninguna | A <opción> (costo si me equivoco) | B <opción> (costo) | elegida: <X> porque <Y>
Movimiento: ninguno | sutil | <qué>
Evitar: 3 patrones máximo
Criterios medibles: 3 máximo, p. ej. contraste >= 4,5:1 | elementos visibles sin desplazarse a 1366x768 | sin desplazamiento horizontal a 375 px
Alcance: archivos o pantallas afectadas | por definir
Por verificar: ninguno | - dato: cómo comprobarlo
```

## Reglas
- Máximo ~26 líneas.
- Valores concretos (fuentes, hex o variables), no adjetivos. Los criterios medibles son números o condiciones que se pueden comprobar con una captura o un script.
- `Alternativas` solo si había dos caminos razonables; la elegida lleva su porqué.
- No incluir código ni rutas inventadas: `Alcance` solo lista lo que se vio.
- `Por verificar` para lo que depende de algo que el usuario no mostró (marca existente, restricciones de accesibilidad).
