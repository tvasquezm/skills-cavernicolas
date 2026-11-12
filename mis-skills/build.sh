#!/usr/bin/env bash
# Empaqueta cada skill en dist/<skill>.zip (carpeta de la skill en la raíz del zip).
# Uso: ./build.sh            -> todas las skills
#      ./build.sh cave-codeo -> solo una
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist

if [ "$#" -gt 0 ]; then skills=("$@"); else
  skills=(); for d in */; do [ -f "${d}SKILL.md" ] && skills+=("${d%/}"); done
fi

for s in "${skills[@]}"; do
  [ -f "$s/SKILL.md" ] || { echo "SKIP $s (sin SKILL.md)"; continue; }
  ver=$(grep -m1 -E '^[[:space:]]+version:' "$s/SKILL.md" | sed -E 's/.*"([^"]+)".*/\1/')
  rm -f "dist/$s.zip"
  zip -rq "dist/$s.zip" "$s" -x "*.git*" "*.DS_Store"
  echo "OK  $s  v${ver:-?}  -> dist/$s.zip"
done
