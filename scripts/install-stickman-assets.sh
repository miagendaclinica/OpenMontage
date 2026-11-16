#!/usr/bin/env bash
# Download the stickman skill's audio/asset library (~490 MB) on demand.
# Media stays gitignored. Text, scripts, and manifests already live in the repo.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT/.agents/skills/directing-stickman-videos/assets"
REPO="https://github.com/kaomei/stickman-video-director.git"
REF="${STICKMAN_REF:-8ef02ece5f12b8c7969fce1009d21653b597d203}"
TMP="$(mktemp -d)"

cleanup() { rm -rf "$TMP"; }
trap cleanup EXIT

echo "==> Downloading stickman assets at $REF"
echo "    This sparse checkout is about 490 MB. It is not committed."

git clone --filter=blob:none --sparse --no-checkout "$REPO" "$TMP/repo"
git -C "$TMP/repo" sparse-checkout set skills/directing-stickman-videos/assets
git -C "$TMP/repo" fetch --depth 1 origin "$REF"
git -C "$TMP/repo" checkout --detach "$REF"

mkdir -p "$DEST"
cp -a "$TMP/repo/skills/directing-stickman-videos/assets/." "$DEST/"

echo "==> Installed into $DEST"
echo "    Check: find \"$DEST\" -type f | wc -l"
