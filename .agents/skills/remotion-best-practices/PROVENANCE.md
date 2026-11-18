# Remotion skills — provenance

The 13 Remotion agent skills under `.agents/skills/` are vendored from:

- **Source**: https://github.com/remotion-dev/skills
- **Vendored commit**: `7e541aa4d7361dfaca0780a565a47307eb7bdfbb`
- **Skill version** (from upstream frontmatter): `4.0.543`
- **Vendor date**: 2026-11-16

## Skills

`remotion-best-practices` (router), `remotion-captions`, `remotion-create`, `remotion-docs`, `remotion-interactivity`, `remotion-license`, `remotion-maps`, `remotion-markup`, `remotion-multimedia`, `remotion-render`, `remotion-saas`, `remotion-studio`, `remotion-upgrade`.

Upstream nests a second copy of each specialist skill inside `remotion-best-practices/` and points the router at `./<skill>/REFERENCE.md`. This repo keeps a single copy of each skill as a sibling, and the router links to `../<skill>/SKILL.md`. That avoids a duplicate tree and a second set of folders at the repository root.

## Preserved `rules/`

`remotion-best-practices/rules/` is the previous OpenMontage Remotion mechanics codex (charts, text animations, trimming, maps, and the rest). It was merged back in after the upstream refresh and is still linked from the router. Do not delete it when re-vendoring.

## Re-sync

```bash
git clone --depth 1 https://github.com/remotion-dev/skills.git /tmp/remotion-skills
# Copy skills/remotion-* into .agents/skills/, keep rules/, and rewrite
# router links from ./<skill>/REFERENCE.md to ../<skill>/SKILL.md.
# Then refresh the commit hash at the top of this file.
```
