# Stickman asset library

The skill text, scripts, tests, and examples in this folder come from
[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)
(`skills/directing-stickman-videos`, MIT, commit `8ef02ece5f12b8c7969fce1009d21653b597d203`).
See `LICENSE`.

The audio and image library under `assets/` is about 490 MB. Those media files
(audio, video, png/jpg, fonts) are gitignored. Manifests and scripts inside
`assets/` are committed so the skill can be read without the download.

Install the library on demand, from the repository root:

```bash
bash scripts/install-stickman-assets.sh
```

The script sparse-checks out `skills/directing-stickman-videos/assets` from the
pinned upstream commit into this folder. Re-run it to refresh a missing library.
