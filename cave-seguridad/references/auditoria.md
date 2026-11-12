# Auditoría por áreas

Solo lectura. Recorre solo las áreas que la superficie confirmada hace relevantes. Cada hit se confirma leyendo el código: un `grep` no es un hallazgo.

## 1. Secretos
- Claves, tokens, contraseñas y cadenas de conexión en código, config, tests, CI y Dockerfiles.
- `.env` versionado o no ignorado; `.gitignore` sin cubrir claves y certificados.
- Historial: `git log -S"<patrón>" --oneline` (solo lectura). Un secreto ya commiteado está comprometido aunque se borre: recomendar rotación.
- Claves privilegiadas en el cliente (`service_role`, admin, secretos en variables públicas como `NEXT_PUBLIC_*` o `VITE_*`).

## 2. Autenticación y sesiones
- Hash de contraseñas (argon2, bcrypt, scrypt); nunca MD5/SHA1/sin sal.
- JWT: algoritmo fijado, `exp`, secreto fuerte, verificación de firma, sin datos sensibles en el payload.
- Cookies: `HttpOnly`, `Secure`, `SameSite`; tokens en `localStorage` como riesgo ante XSS.
- Límite de intentos, enumeración de usuarios, flujos de recuperación, MFA, expiración y revocación de sesión.

## 3. Autorización
- Verificación en el servidor en cada endpoint y acción, no solo en la UI.
- IDOR/BOLA: ¿el recurso se filtra por el usuario o tenant autenticado?
- Asignación masiva (campos como `role` o `isAdmin` aceptados del cliente).
- Rutas administrativas y funciones internas expuestas.
- Políticas a nivel de base de datos (RLS u equivalentes) activas y sin bypass.

## 4. Entradas y salidas
- SQL/NoSQL: consultas concatenadas, `raw`, filtros construidos con entrada.
- Comandos: `exec`, `spawn` con shell, `eval`, `Function`.
- Rutas de archivo: path traversal, nombres controlados por el usuario.
- XSS: `innerHTML`, `dangerouslySetInnerHTML`, plantillas sin escape, URLs `javascript:`.
- SSRF y redirecciones abiertas: URLs controladas por el usuario usadas en el servidor o en `redirect`.
- Deserialización insegura, XXE, inyección de plantillas, ReDoS.
- Validación en el servidor con esquema y lista permitida, no solo en el cliente.

## 5. Uploads
Tipo real (no solo extensión ni MIME declarado), tamaño máximo, nombre regenerado, almacenamiento fuera del webroot o en bucket privado, sin ejecución, URLs firmadas con expiración.

## 6. Configuración web
CORS (sin `*` con credenciales ni orígenes reflejados), CSRF en acciones con cookies, CSP, HSTS, `X-Content-Type-Options`, `Referrer-Policy`, errores verbosos, modo debug o stack traces en producción, TLS y verificación de certificados activa.

## 7. Criptografía
Algoritmos rotos (MD5, SHA1, DES, ECB), aleatoriedad no criptográfica para tokens (`Math.random`), claves o IV fijos, TLS con verificación desactivada, cifrado propio.

## 8. Datos y registros
Datos personales o tokens en logs, URLs y mensajes de error; datos sensibles sin cifrar en reposo; backups sin protección; retención indefinida; datos de producción en fixtures o tests.

## 9. APIs
Límite de tasa, paginación con tope, exceso de datos en respuestas, endpoints sin auth olvidados, documentación o introspección expuesta (Swagger, GraphQL) en producción, versiones antiguas activas.

## 10. Infraestructura, CI y contenedores
- Docker: usuario root, imagen `latest`, secretos en capas o `ARG`, puertos innecesarios.
- IaC: buckets o bases públicas, permisos IAM amplios (`*`), grupos de seguridad abiertos.
- CI (GitHub Actions): `pull_request_target` con código no confiable, permisos de `GITHUB_TOKEN` amplios, acciones de terceros sin fijar por SHA, secretos impresos en logs.

## 11. Frontend y móvil
Secretos en el bundle, source maps públicos, tokens en almacenamiento inseguro, deep links sin validar, `postMessage` sin verificar origen, dependencias de CDN sin integridad (SRI).

## 12. IA y LLM (si el proyecto integra modelos)
Inyección de prompts desde contenido no confiable, secretos en prompts, salida del modelo usada sin sanitizar (HTML, SQL, shell), herramientas o agentes con permisos excesivos, datos personales enviados a terceros sin base, claves de API en el cliente.

## Método
Búsquedas de solo lectura sobre lo del alcance, leer el contexto de cada coincidencia, descartar falsos positivos (valores de ejemplo, tests, comentarios) y anotar solo lo confirmado. Si no puedes confirmar, es `por verificar` con el dato que falta.
