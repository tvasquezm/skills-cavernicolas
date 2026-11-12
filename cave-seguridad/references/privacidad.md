# Privacidad y cumplimiento

Señala indicios técnicos, no da asesoría legal: la conclusión jurídica la confirma un abogado o el responsable de datos. Las normas cambian: con web, verifica el estado vigente antes de citar fechas y registra la fecha de consulta.

## Marco aplicable (según usuarios y datos)
- **Chile:** Ley 19.628 y Ley 21.719, que la reemplaza y crea la Agencia de Protección de Datos Personales. La fecha de entrada en vigencia de la 21.719 ha estado sujeta a cambios y a proyectos que la posponen: no cites una fecha de memoria. Con web, consulta el estado vigente (texto publicado y vigencia) y registra fuente y fecha en `Cobertura`; sin web, di que la vigencia está `por verificar`. Ley 21.663 (marco de ciberseguridad) si el proyecto es de un servicio esencial u operador de importancia vital. Ley 21.459 (delitos informáticos) como contexto.
- **UE o residentes UE:** GDPR. **California:** CCPA/CPRA. **Brasil:** LGPD. Solo si el proyecto tiene usuarios allí.

## Qué revisar en el código y la configuración
1. **Inventario:** qué datos personales se recogen, dónde se almacenan y quién los recibe. Datos sensibles (salud, biometría, origen, opiniones, situación socioeconómica) y de menores con cuidado reforzado.
2. **Minimización y finalidad:** campos recogidos que no se usan; datos reutilizados para otro fin.
3. **Base de licitud y consentimiento:** consentimiento explícito, separado y revocable cuando corresponda; registro de cuándo y qué se aceptó.
4. **Derechos del titular:** existe forma técnica de acceder, rectificar, suprimir, oponerse, bloquear y portar los datos.
5. **Retención:** plazos definidos y borrado real (incluye backups, logs y copias en terceros).
6. **Terceros y transferencias:** analítica, pagos, correo, modelos de IA, hosting fuera del país; contratos o configuración de encargado; datos enviados de más.
7. **Seguridad del tratamiento:** cifrado en tránsito y en reposo, control de acceso, pseudonimización, registro de accesos a datos personales.
8. **Brechas:** existe forma de detectar, registrar y notificar un incidente.
9. **Decisiones automatizadas y perfilado:** señalarlas si existen.
10. **Privacidad por diseño y por defecto:** configuraciones que exponen más de lo necesario por defecto.
11. **Evaluación de impacto:** señalar cuándo el tratamiento (datos sensibles a gran escala, vigilancia, perfilado) probablemente la exige.

## Severidad típica
Exposición masiva o sin control de datos personales: CRÍTICO. Datos personales en logs o enviados a terceros sin base, sin retención definida o sin forma de ejercer derechos: MEDIO a ALTO según volumen y sensibilidad. Faltas documentales sin evidencia técnica: nota, no hallazgo.
