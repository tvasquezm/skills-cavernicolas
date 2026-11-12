#!/usr/bin/env bash
# Empaqueta cada skill en dist/<skill>.zip (carpeta de la skill en la raíz del zip).
# Uso: ./build.sh            -> todas las skills (raíz y diseno/)
#      ./build.sh cave-codeo -> solo una (también acepta nombres de diseno/, ej. impeccable)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist

if [ "$#" -gt 0 ]; then skills=("$@"); else
  skills=(); for d in */ diseno/*/; do [ -f "${d}SKILL.md" ] && skills+=("${d%/}"); done
fi

root="$PWD"
for p in "${skills[@]}"; do
  p="${p#./}"; [ -f "$p/SKILL.md" ] || [ -f "diseno/$p/SKILL.md" ] && [ ! -f "$p/SKILL.md" ] && p="diseno/$p"
  [ -f "$p/SKILL.md" ] || { echo "SKIP $p (sin SKILL.md)"; continue; }
  s=$(basename "$p"); parent=$(dirname "$p")
  ver=$(grep -m1 -E '^[[:space:]]+version:' "$p/SKILL.md" | sed -E 's/.*"([^"]+)".*/\1/' || true)
  [ -n "$ver" ] || ver=$(grep -m1 -E '^version:' "$p/SKILL.md" | sed -E 's/version:[[:space:]]*"?([^"]+)"?/\1/' || true)
  rm -f "dist/$s.zip"
  (cd "$parent" && zip -rq "$root/dist/$s.zip" "$s" -x "*.git*" "*.DS_Store")
  echo "OK  $s  v${ver:-?}  -> dist/$s.zip"
done
