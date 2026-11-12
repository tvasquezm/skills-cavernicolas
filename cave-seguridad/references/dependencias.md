# Dependencias, CI y contenedores

## Qué inspeccionar (solo lectura)
- Manifiestos y lockfiles (`package.json` y su lockfile, `requirements*.txt`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `pom.xml`, `Gemfile`...). Sin lockfile: hallazgo de reproducibilidad.
- Versiones con avisos conocidos, paquetes abandonados, nombres sospechosos (typosquatting), scripts `postinstall` o de instalación que ejecutan código.
- Rangos abiertos (`*`, `latest`) en producción.
- Dockerfiles: imagen base y versión, usuario, capas con secretos.
- Workflows de CI: acciones de terceros sin fijar por SHA, permisos del token.

## Fuentes de avisos
OSV.dev, GitHub Advisory Database, NVD, CISA KEV (explotación activa), EPSS (probabilidad de explotación), avisos del propio proveedor o mantenedor.
- Con web: consulta por paquete y versión reales, y registra fuente y fecha en `Cobertura`.
- Sin web: no cites CVE de memoria como confirmados. Marca `por verificar` y entrega el comando local.

## Priorización
Primero lo que está en KEV o con EPSS alto, y lo alcanzable desde el código del proyecto. Una dependencia vulnerable que el código no invoca es MEDIO o BAJO con la razón escrita. No actualices nada: la actualización es un microplan aparte.

## Herramientas locales (comandos para `Ejecuta en tu equipo:`)
Usa solo las que el repositorio sugiere por su stack y verifica el gestor real antes de escribirlas.
- Dependencias: `npm audit`, `pip-audit`, `cargo audit`, `govulncheck ./...`, `osv-scanner`, `trivy fs .`
- Secretos: `gitleaks detect`, `trufflehog`
- Código: `semgrep --config auto`
- IaC y contenedores: `checkov -d .`, `trivy config .`, `trivy image <imagen>`

Corre aquí solo las que ya existan en el entorno y no escriban en el proyecto. Sin red o herramienta: `OMITIDO` con el motivo.
