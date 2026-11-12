# Informe

Leer antes de entregar. El informe es el único entregable.

## Severidad (por impacto y explotabilidad reales)
- **CRÍTICO:** ejecución remota, bypass de autenticación, secreto de producción expuesto, exposición masiva de datos personales o inyección explotable sin credenciales.
- **ALTO:** IDOR o escalada de privilegios, inyección que exige sesión, XSS almacenado, criptografía rota sobre datos sensibles, dependencia con explotación activa (CISA KEV) alcanzable desde el código.
- **MEDIO:** debilidad que requiere condiciones adicionales, falta de límites de tasa, CORS permisivo sin credenciales, datos personales en logs, dependencia vulnerable sin ruta de explotación clara.
- **BAJO:** endurecimiento: cabeceras, mensajes verbosos sin datos sensibles, buenas prácticas.

Reglas: sin evidencia confirmada no se asigna crítico ni alto; si la gravedad potencial es alta pero falta confirmar, se reporta `ALTO (por verificar)` y el veredicto queda `CON RESERVAS`. No rebajes severidad por brevedad ni la subas por alarma.

## Formato
```
INFORME DE SEGURIDAD - <proyecto>
Fecha: | Alcance: cambios | completo | rutas | Estado del repo: <commit o "sin Git">
Veredicto: BLOQUEADO | CON RESERVAS | SIN HALLAZGOS EN LO REVISADO
Cobertura: revisado: áreas y archivos | no revisado: ... | fuentes consultadas: nombre + fecha | omitido: control + motivo

Hallazgos
S-01 [CRÍTICO|ALTO|MEDIO|BAJO] Título (CWE-nnn / OWASP)
  Evidencia: archivo:línea - confirmado | por verificar
  Riesgo: qué puede hacer un atacante y con qué impacto
  Corrección: qué cambiar, en lenguaje natural
  Verificación: caso negativo o prueba que demuestra el arreglo
S-02 ...

Notas: fuera de alcance, sin evidencia suficiente o supuestos
```
Ordena por severidad. Un hallazgo por causa raíz, no por ocurrencia: agrupa las ocurrencias bajo el mismo ID.

## Bloque HALLAZGOS (para `cave-planificacion`)
Cuando el usuario pide pasar las correcciones al plan, entrega solo este bloque, sin valores de secretos:
```
HALLAZGOS - <proyecto> - <fecha>
S-01 | severidad | título | archivos | corrección | verificación
```
Termina con: `Pega HALLAZGOS en /cave-planificacion para priorizar; se ejecutan con /cave-codeo.`

## Secretos expuestos
Recomendar siempre rotar la credencial y revisar su uso, además de retirarla del código. Retirarla del repositorio no la descompromete si estuvo en el historial.

## Controles omitidos
`OMITIDO` nunca cuenta como aprobado. Cada uno lleva motivo y comando exacto en `Ejecuta en tu equipo:` (gestor y scripts verificados en el repositorio). Con controles requeridos omitidos el veredicto no puede ser `SIN HALLAZGOS EN LO REVISADO`.

## Reauditoría
Tras las correcciones, un hallazgo se da por resuelto solo si el síntoma se confirma antes y después en el código real y el caso negativo de `Verificación` pasa. Si no se pudo ejecutar, queda `por verificar`.
