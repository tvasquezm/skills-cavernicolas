# Verificación

Registro interno: no se informa en el cierre salvo fallo real, omisión sin comando local o hallazgo.

**Sin evidencia no hay "pasó".** Cada control lleva comando real y resultado. Lo no ejecutado es `OMITIDO` con motivo y nunca cuenta como aprobado.

## Comando
Usa el script real del proyecto (`package.json`, `Makefile`, `pyproject.toml`...). Focal primero (un archivo o una prueba). Ejemplos a adaptar tras verificar el gestor real, no a asumir:
- Node: `npm test -- <ruta>`, `npx vitest run <ruta>`, `npx jest <ruta>`
- Python: `pytest <ruta>::<prueba> -q`
- Go: `go test ./<paquete> -run <Nombre>`
- Rust: `cargo test <nombre>`
- Java: `mvn -Dtest=<Clase> test`; .NET: `dotnet test --filter <nombre>`

## Controles
1. **Pasan:** las pruebas nuevas y las del mismo archivo o módulo que ya existían.
2. **Fallan por la razón correcta:** para cubrir un defecto, reprodúcelo antes (falla) y después (pasa). Sin acceso al estado "antes" sin tocar código del usuario, dilo como `por verificar` en vez de revertir nada.
3. **Estabilidad:** si hay tiempo, azar, orden, red o concurrencia, ejecuta de nuevo; una prueba que falla a veces se corrige en la prueba.
4. **Diff real:** `git status` y `git diff` (sin Git, `diff -ruN orig work`): solo archivos de prueba, fixtures y mocks; sin reformateos ni temporales.
5. **Secretos:** ninguna credencial ni dato real en fixtures.
6. **Cobertura:** solo si el proyecto ya la mide, sobre lo tocado, y como dato, no como meta.

## Un fallo
- **Falla la prueba por error mío:** corrige la prueba y repite ese control; sin hipótesis nueva no hay reintento; al tercer intento, detente.
- **Falla porque el código está mal:** es un hallazgo. No toques producción. Deja la prueba como evidencia solo si el usuario lo aprobó; si no, repórtala y no la dejes rota sin avisar.

## Entorno
Instala solo lo declarado en el lockfile (instalación congelada, sin scripts, sin tocar manifiestos). Sin red o herramienta: no inventes; `OMITIDO` y el comando va en `Ejecuta en tu equipo:`. Una verificación requerida `OMITIDO` deja el trabajo en `ejecutado, por verificar`.
