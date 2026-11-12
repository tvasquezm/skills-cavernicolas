# Diseño de pruebas

## Antes de escribir
Identifica el contrato del código: entradas, salidas, errores y efectos. Pruébalo por su interfaz pública. Copia la convención de una prueba existente (framework, carpeta, nombre, estilo de aserción, fixtures). Sin pruebas previas: usa el framework que el proyecto ya declare; si no hay ninguno, no instales uno: detente y pide decisión.

## Niveles
- **Unitaria:** lógica pura y reglas de negocio. Rápida y sin E/S.
- **Integración:** módulos reales entre sí, con base de datos o servicios de prueba aislados, solo si el proyecto ya lo soporta.
- **Contrato o API:** formas de petición y respuesta, códigos de estado, errores.
- **E2E:** solo si el proyecto ya tiene runner; pocas y para flujos críticos.
Elige el nivel más bajo que demuestre el comportamiento.

## Qué cubrir (por comportamiento)
1. Camino feliz.
2. Bordes: vacío, nulo, mínimo, máximo, límites exactos, unicode, zonas horarias.
3. Errores: entradas inválidas, dependencias que fallan, tiempos agotados.
4. **Negativos de seguridad** cuando el cambio toque auth, permisos, datos personales o entrada hacia SQL/shell/archivos/HTML: acceso a recurso ajeno, rol insuficiente, entrada maliciosa o malformada, sin sesión.
5. Regresión: el caso exacto de un bug corregido.

## Reglas de calidad
- Una razón de fallo por prueba; nombre que dice regla y condición (`rechaza_descuento_mayor_al_100`).
- Arrange / Act / Assert visibles. Aserciones específicas sobre valores, no solo "no lanza error" ni `toBeTruthy`.
- Deterministas: sin `sleep`, sin fecha ni hora reales (congela el reloj), sin azar sin semilla, sin depender del orden.
- Aisladas: datos propios por prueba, limpieza garantizada, sin estado compartido.
- Dobles de prueba solo en los bordes del sistema (red, tiempo, correo, pagos). No simules lo que estás probando.
- Snapshots solo para salidas estables y pequeñas, nunca generados a ciegas.
- No pruebes código de terceros ni detalles privados de implementación.
- Datos de prueba sintéticos. Nunca personas reales ni secretos.

## Qué no hacer
- Prueba que pasa siempre (aserción vacía, mock que devuelve lo esperado).
- Copiar la lógica del código dentro de la prueba para calcular el resultado esperado.
- Subir cobertura por cobertura: el objetivo es detectar defectos, no un porcentaje.
