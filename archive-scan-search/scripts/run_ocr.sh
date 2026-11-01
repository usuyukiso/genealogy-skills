#!/bin/zsh
# OCR a whole collection in N parallel workers, then wait until every frame has a text.
#   run_ocr.sh "<collection dir>" [workers=4]
# Output: "<collection dir>/_ocr/<subfolder>__<frame>.txt". Re-running skips done frames.
# Waits by counting files (never by `pgrep -f`, which matches the waiting loop itself).
set -u
DIR="$1"; N="${2:-4}"
HERE="${0:A:h}"
BIN="${TMPDIR:-/tmp}/scan_ocr"
[ -x "$BIN" ] || swiftc -O "$HERE/ocr.swift" -o "$BIN" || exit 1
mkdir -p "$DIR/_ocr"
TOTAL=$(find "$DIR" -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.jxl' -o -iname '*.png' \) -not -path '*/_ocr/*' | wc -l | tr -d ' ')
FOLDERS=("${(@f)$(cd "$DIR" && ls -d */ | sed 's:/$::' | grep -v '^_ocr$')}")
PIDS=()
for ((w = 0; w < N; w++)); do
  (for ((i = w + 1; i <= ${#FOLDERS}; i += N)); do "$BIN" "$DIR/${FOLDERS[i]}" "$DIR/_ocr"; done) \
    > "$DIR/_ocr/.worker$w.log" 2>&1 &
  PIDS+=($!)
done
echo "OCR: $TOTAL frames, $N workers"
while true; do
  ALIVE=0
  for p in $PIDS; do kill -0 $p 2>/dev/null && ALIVE=1; done
  [ $ALIVE -eq 0 ] && break
  sleep 30
done
grep -h FAIL "$DIR"/_ocr/.worker*.log 2>/dev/null
echo "done $(ls "$DIR/_ocr" | grep -c '\.txt$')/$TOTAL"
rm -f "$DIR"/_ocr/.worker*.log
