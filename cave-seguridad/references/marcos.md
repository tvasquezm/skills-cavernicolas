# Marcos de referencia

Úsalos para clasificar y mapear hallazgos, no para listar todo el marco. Las ediciones cambian: con web, confirma la vigente y registra la fecha en `Cobertura`; sin web, indica que el mapeo usa la edición que conoces.

| Marco | Para qué |
|---|---|
| OWASP Top 10 (web) | Mapeo de categorías de riesgo en aplicaciones web |
| OWASP ASVS | Nivel de verificación y requisitos concretos por área (auth, sesiones, validación, criptografía) |
| OWASP API Security Top 10 | BOLA, autenticación rota, exposición excesiva, falta de límites |
| OWASP Top 10 para LLM | Inyección de prompts, salida insegura, agentes con exceso de permisos |
| OWASP MASVS / MASTG | Aplicaciones móviles |
| OWASP Cheat Sheet Series | Corrección recomendada por tema (contraseñas, CSRF, XSS, SSRF, JWT) |
| CWE y CWE Top 25 | Identificador de la debilidad en cada hallazgo |
| CISA KEV | Vulnerabilidades con explotación activa: elevan la prioridad |
| NIST SSDF (SP 800-218) y CIS Controls | Prácticas de desarrollo seguro y controles de base |

## Uso
- Cada hallazgo lleva un CWE y, si aplica, la categoría OWASP. Si no estás seguro del identificador, omítelo antes que inventarlo.
- Al elegir la corrección, apóyate en la hoja de OWASP correspondiente y cítala por nombre.
- ASVS sirve para fijar el nivel exigible: L1 base, L2 la mayoría de las apps con datos sensibles, L3 alto riesgo. Si el usuario no lo definió, asume L2 y dilo como supuesto.
