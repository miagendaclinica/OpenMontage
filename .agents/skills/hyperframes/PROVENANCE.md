# HyperFrames skills — provenance

## Current upstream (refreshed 2026-11-16)

These skills are vendored from the HyperFrames monorepo so they travel with this repo:

- **Source**: https://github.com/heygen-com/hyperframes
- **Vendored commit**: `4067efc454382463979f0625e8e031a73ff05b9d`
- **Paths**: `skills/hyperframes`, `skills/hyperframes-cli`, `skills/hyperframes-registry`, and the related skills that commit ships: `media-use`, `remotion-to-hyperframes`, `figma`, `reverse-any-video`, `slideshow`, `style-sampling`.

Upstream folded the old split (`hyperframes-core`, `hyperframes-creative`, `hyperframes-media`, `hyperframes-animation`, `motion-graphics`, `music-to-video`, `website-to-video`) into the `hyperframes` skill and a smaller skills directory. Those older directories are **still in this repo** from the v0.7.17 vendor (`3351fb1a`, 2026-06-27), because OpenMontage stage directors and `skills/core/hyperframes.md` still route to them. Prefer the refreshed `hyperframes` skill when the two disagree.

## Re-sync

```bash
git clone --depth 1 https://github.com/heygen-com/hyperframes.git /tmp/hyperframes
HF=/tmp/hyperframes
for d in hyperframes hyperframes-cli hyperframes-registry media-use \
         remotion-to-hyperframes figma reverse-any-video slideshow style-sampling; do
  rm -rf ".agents/skills/$d"
  cp -a "$HF/skills/$d" ".agents/skills/$d"
done
# Restore this PROVENANCE.md (the upstream skill does not ship it) and
# update the commit hash above. Re-point .claude/skills symlinks if needed.
```
