# Formato del bloque DIRECCION DE DISENO

Una dirección visual por tarea. Si el usuario ya fijó una (por ejemplo en el proyecto), se respeta y no se reemplaza.

```
DIRECCION DE DISENO - <proyecto o pantalla>
Fecha:
Skill: cave-diseno v<versión>
Tarea: <una línea>
Skills usadas: base <skill> | estilo <skill> | ninguno | complemento <skill> | ninguno
No instaladas: ninguna | - <skill>
Tipografía: títulos <fuente> | texto <fuente>
Paleta: fondo | texto | acento (valores o variables)
Densidad y layout: <una línea>
Movimiento: ninguno | sutil | <qué>
Evitar: 3 patrones máximo
Alcance: archivos o pantallas afectadas | por definir
Por verificar: ninguno | - dato: cómo comprobarlo
```

## Reglas
- Máximo ~20 líneas.
- Valores concretos (fuentes, hex o variables), no adjetivos.
- No incluir código ni rutas inventadas: `Alcance` solo lista lo que se vio.
- `Por verificar` para lo que depende de algo que el usuario no mostró (marca existente, restricciones de accesibilidad).
