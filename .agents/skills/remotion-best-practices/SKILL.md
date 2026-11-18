---
name: remotion-best-practices
description: Router for all Remotion skills
version: 4.0.543
---

## Preserve user changes

Users may make edits in the code outside of the conversation.

If you detect a surprising change made in the meanwhile, don't overwrite it, assume it was intentional or ask for confirmation.

## Creating a video

If the user asks to make, create, or build a new video or composition, load [Create a new Remotion video](../remotion-create/SKILL.md), whether or not a Remotion project already exists.

## New project setup

If no Remotion project currently exists, load [Create a new Remotion project](../remotion-create/SKILL.md)

## React Markup Best Practices

If you are writing Remotion React Markup, load [Remotion Markup Best Practices](../remotion-markup/SKILL.md)

## Maps

For static maps, animated routes and markers, geographic explainers, Mapbox, MapLibre, MapTiler, GeoJSON, or 3D geographic flyovers, load [Remotion Maps](../remotion-maps/SKILL.md).

## Multimedia

For achieving multimedia tasks in the browser, such as trimming, cropping videos, or getting metadata from them, load [Remotion Multimedia](../remotion-multimedia/SKILL.md)

For video matting, background removal, or placing content behind a subject,
load [Remotion Markup](../remotion-markup/SKILL.md).

## Interactivity

New markup is editable in Studio by default. When writing or restructuring markup, load [Interactivity Best Practices](../remotion-interactivity/SKILL.md).

## Open the preview

If the user asks to "make" a video, "create" a video, etc.
Don't render the video by default unless they are very explicit. They want to instead see an interactive preview.
As soon as the project can run, start Studio and open the preview in the browser before building or editing the composition. Keep it open while you work so the user can watch progress and steer.

### If you are using Cursor

Run Studio without `--no-open` so it opens the browser automatically:

```bash
npx remotion studio
```

### If you are using another agent client with an in-app browser

You can use the command above to let Studio open the browser, or run:

```bash
npx remotion studio --no-open
```

This will start a long-running process and print the server URL for the preview.  
If the server is already started, it will print the URL.
If you use `--no-open`, open the exact printed URL in the in-app browser and verify that Studio loads. Once a composition exists, verify that its video preview loads. If you cannot open it there, run Studio without `--no-open`.
You can visit a specific composition by navigating to `/[composition-id]`, for example `http://localhost:3000/MapAnimation`.

:::note
The Studio supports WebMCP tools.
:::

### If you do not have an in-app browser

This will open the Studio in the browser or refocus it if it is already open.

```bash
npx remotion studio
```

### More options

To launch a project in Remotion Studio, open its exact local URL, or configure Studio CLI flags, load [Remotion Studio](../remotion-studio/SKILL.md).

## Render the video

Only render if the user is very explicit in asking for it.  
E.g. "Render the video", "Export", "Give me the MP4".

The preview also has a more intuitive rendering interface, so consider using it instead of the command line for rendering.

```
npx remotion render
```

For more options, see [Rendering](../remotion-render/SKILL.md).

For advanced rendering beyond simple `npx remotion render`, see: [Rendering Best Practices](../remotion-render/SKILL.md)

## Captions

When working with Captions, load [Remotion Captions](../remotion-captions/SKILL.md).

## Creating a SaaS, automation or application

Use the [Remotion SaaS skill](../remotion-saas/SKILL.md) for knowledge about Remotion-powered SaaS apps, such as `<Player>`, rendering on Lambda, Vercel, Cloudflare, via Express.js, client-side rendering, or for finding the right SaaS template.

## Looking up Remotion APIs and documentation

To find and read current Remotion documentation, load [Remotion Docs](../remotion-docs/SKILL.md).

## Licensing

For Remotion license information, FAQs, terms, or buying a license, load [Remotion License](../remotion-license/SKILL.md).

## Upgrading

To upgrade Remotion, related packages, compatible Mediabunny packages, and installed Remotion Agent Skills, load [Remotion Upgrade](../remotion-upgrade/SKILL.md).

## OpenMontage preserved rules

This repository keeps the previous `rules/` directory next to the current Remotion skill router. Those files still work. They are the mechanics codex for `remotion-composer` (Remotion 4.0.484). Read a rule when its topic matches. The sibling skills linked above are the current upstream guides; prefer them when they cover the same topic, and keep `rules/` for the composer patterns already used here (charts, text animations, trimming, maps, and the rest of the list).

- [rules/3d.md](rules/3d.md)
- [rules/animations.md](rules/animations.md)
- [rules/assets.md](rules/assets.md)
- [rules/audio-visualization.md](rules/audio-visualization.md)
- [rules/audio.md](rules/audio.md)
- [rules/calculate-metadata.md](rules/calculate-metadata.md)
- [rules/can-decode.md](rules/can-decode.md)
- [rules/charts.md](rules/charts.md)
- [rules/compositions.md](rules/compositions.md)
- [rules/display-captions.md](rules/display-captions.md)
- [rules/extract-frames.md](rules/extract-frames.md)
- [rules/ffmpeg.md](rules/ffmpeg.md)
- [rules/fonts.md](rules/fonts.md)
- [rules/get-audio-duration.md](rules/get-audio-duration.md)
- [rules/get-video-dimensions.md](rules/get-video-dimensions.md)
- [rules/get-video-duration.md](rules/get-video-duration.md)
- [rules/gifs.md](rules/gifs.md)
- [rules/images.md](rules/images.md)
- [rules/import-srt-captions.md](rules/import-srt-captions.md)
- [rules/light-leaks.md](rules/light-leaks.md)
- [rules/lottie.md](rules/lottie.md)
- [rules/maps.md](rules/maps.md)
- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md)
- [rules/measuring-text.md](rules/measuring-text.md)
- [rules/parameters.md](rules/parameters.md)
- [rules/sequencing.md](rules/sequencing.md)
- [rules/sfx.md](rules/sfx.md)
- [rules/subtitles.md](rules/subtitles.md)
- [rules/tailwind.md](rules/tailwind.md)
- [rules/text-animations.md](rules/text-animations.md)
- [rules/timing.md](rules/timing.md)
- [rules/transcribe-captions.md](rules/transcribe-captions.md)
- [rules/transitions.md](rules/transitions.md)
- [rules/transparent-videos.md](rules/transparent-videos.md)
- [rules/trimming.md](rules/trimming.md)
- [rules/videos.md](rules/videos.md)
- [rules/voiceover.md](rules/voiceover.md)
