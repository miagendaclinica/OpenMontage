---
name: motion-cinco-efectos
description: Checklist of ten motion techniques that make code-based motion graphics (Remotion/HyperFrames/GSAP) feel professional instead of "PowerPoint". Apply to every explainer or motion scene.
---

# Motion house rules (ten effects)

Apply all of them unless the brief says otherwise. Never move anything linearly; use springs or ease-in-out curves.

1. **Mask reveals for text.** Words slide up from behind an invisible clip line (overflow hidden / clip-path), staggered per word or line, instead of fading in.
2. **Chained motion.** One element enters and pushes or triggers the next (collision, nudge, connecting line drawing between them). Scenes read as cause and effect, not independent pops.
3. **Camera follows the action.** Animate a virtual camera (scale + translate on a parent container): push in on what matters, track it while it moves, then pull back out.
4. **Object morphs into the next scene.** A card, icon or shape expands to fill the frame and becomes the next scene's UI or background (shared-element / circular mask wipe transition).
5. **Sync entries to narration.** Use word-level timestamps (whisper transcript) to place keyframes: when the voice says a number, that number appears; when it names an action, that animation starts on that word.

6. **Easing with a small bounce.** Entrances end with a slight overshoot (GSAP `back.out(1.7)`, Remotion `spring` with low damping). Linear = robotic.
7. **Staggered entrances.** Sibling elements (lists, icons, characters, grid items) enter one after another (stagger ~0.08-0.15 s), never all at once.
8. **Parallax depth.** Split each scene into background, midground and foreground layers; on any camera move, translate them at different rates (e.g. 0.2x / 0.5x / 1x).
9. **Constant micro-movement.** No frame is ever fully static: during holds add a slow push-in (scale 1.00 to 1.05 over the hold), gentle float or sway, or ambient loops (steam, blinking cursor, pulsing dot).
10. **Light-bar ("lightsaber") reveal.** Two glowing horizontal bars appear and move apart; the clip mask between them opens from the center to reveal a word, object or block of text. With filmed footage of a person, anchor the bars between their hands (needs hand tracking or manual keyframes).

Look reference: dark background (#0A0A0A) with a soft central radial glow, glassmorphism cards with thin borders, one accent color (swap for the brand palette), large serif numerals for section numbers, clean sans-serif UI text, small word-by-word captions at bottom center.
