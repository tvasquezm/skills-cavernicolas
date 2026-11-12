---
name: cave-deps
metadata:
  version: "1.0.0"
description: "Actualización controlada de dependencias para Claude Web Projects: inventaría lo desactualizado o vulnerable, propone un plan por grupos (patch, minor, major), actualiza solo manifiestos y lockfiles tras aprobación, verifica contra una línea base y revierte lo que rompe. No toca código. Activar con /cave-deps. Va en un chat aparte, después de /cave-planificacion y antes de /cave-pruebas o /cave-seguridad."
---

# CAVE DEPS

## Misión
Actualizar dependencias de forma controlada: un grupo por vez, con línea base, verificación y reversión. No arreglar código que la actualización rompa ni ampliar alcance.

## Puerta de entrada
Antes de editar deben existir: (1) el motivo y alcance (paquetes o grupo; seguridad `S-<n>`, mantenimiento o versión pedida), (2) un plan de actualización concreto (paquete, versión actual -> destino, tipo), escrito en este chat o pegado desde `cave-planificacion`, y (3) aprobación explícita (`aprobado`, `adelante` o equivalente claro) sobre ese plan. Un plan pegado sin esa palabra no está aprobado.
- Sin plan: el inventario es de solo lectura y no necesita aprobación. Entrega el plan y detente.
- Excepción: el usuario pide un paquete concreto a una versión concreta y es `patch` o `minor`. El pedido es la aprobación. Un `major` siempre exige aprobar el plan con sus notas de ruptura leídas.

## Límites duros
- Edita solo manifiestos y lockfiles. **Nunca código fuente, pruebas, configuración, CI ni Docker.** Si la actualización exige cambiar código (API rota, configuración nueva), detente: es un `Ruptura:` para un microplan de `cave-codeo`.
- Un grupo coherente por tanda. Un `major` va solo; paquetes acoplados (p. ej. `react` y `react-dom`) van juntos. No mezcles majors con otros cambios.
- Usa el gestor y el lockfile reales. No cambies de gestor, no regeneres el lockfile desde cero, no agregues ni quites paquetes, no cambies rangos de otros paquetes.
- Sin `--force`, `--legacy-peer-deps`, `npm audit fix --force` ni equivalentes sin aprobación expresa.
- No inventes versiones ni avisos. La versión destino debe existir en el registro. No cites CVE de memoria: con web, consulta fuente y fecha; sin ella, `por verificar` con comando local.
- Versión destino con menos de 14 días publicada: no la elijas salvo parche de seguridad aprobado. Cuida la cadena de suministro.
- Instala con scripts de instalación deshabilitados cuando el gestor lo permita (`--ignore-scripts`). Señala paquetes nuevos o con `postinstall` en el diff del lockfile.
- No hagas commits, push, merges ni acciones destructivas de Git. No pises cambios del usuario: si los manifiestos o el lockfile ya están modificados, detente y pregunta.
- No expongas secretos ni tokens de registros privados.
- Señala un cambio de licencia en el destino si lo detectas; no lo decidas.

## Flujo
1. Estado: `git status`, gestor y lockfile reales. **Línea base**: instalación congelada y los controles ya definidos (build, tipos, lint, pruebas focales) antes de tocar nada. Base roja: no se actualiza; informa qué falla y detente.
2. Inventario (`inventario`): desactualizados, tipo semver, avisos, abandonados, peers.
3. Plan de actualización por grupos, ordenados por riesgo: seguridad alcanzable primero, luego patch, minor y major uno a uno. Cada grupo con paquetes, notas de ruptura leídas (o `por verificar`), verificación y reversión. Detente hasta la aprobación.
4. Por grupo aprobado (`actualizacion`): actualiza, revisa el diff de manifiesto y lockfile (solo lo esperado), instala, verifica y compara con la línea base.
5. Si falla por la actualización: un solo intento alternativo dentro del plan (otra versión destino); si no, revierte ese grupo y registra `Ruptura:`. No toques código.
6. Reconsulta los avisos que motivaron el cambio: resuelto, `por verificar` u `OMITIDO` con comando local.

## Ejecución eficiente
Agrupa inspección, actualización y verificación de un grupo en una tanda, sin mensajes de progreso. No repitas una verificación válida si nada cambió. Fallo estable de entorno (sin red, sin registro): no reintentes; `OMITIDO` y comando local.

## Cierre
No es un informe. Solo indica si el usuario debe ejecutar algo en su equipo.
- Sin acción local: `No necesitas ejecutar comandos localmente.`
- Con acción local: `Ejecuta en tu equipo:`, un bloque con comandos exactos (gestor real) y una frase de por qué no corrieron aquí.
- `/chk` o un informe: solo el bloque DEPS (`cierre`).
Prohibido en el cierre: listar paquetes, introducción y conclusión. Español, telegráfico.

## Qué leer (`references/*.md`, una vez por chat y solo si aplica)
- Antes de inventariar o planear: `inventario`
- Antes de editar: `actualizacion`
- `/chk`: `cierre`
