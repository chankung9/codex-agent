# Minimal Themed Color Controls

## Goal
Allow hello-agent users to adjust the interface text and background colors using icon-only controls that match the existing theme.

## Requirements
1. **Font Color Icon**
   - Icon: `🅰️` glyph, or an equivalent monochrome/vector icon rendered in the hello-agent accent color.
   - Placement: Top-right corner of the UI, immediately to the left of the background icon.
   - Behavior: Opens a theme-aligned color picker (popover or modal) that updates the global CSS variable `--text-color`.
   - Persistence: Selected color must be saved to `localStorage` so it survives reloads.

2. **Background Color Icon**
   - Icon: `🎨` glyph, or a minimal palette glyph following the theme’s accent color.
   - Placement: Top-right corner, immediately to the right of the text icon.
   - Behavior: Opens the same style of color picker as the font icon and updates global `--bg-color`.
   - Persistence: Selected color saved to `localStorage`.

3. **Style & Accessibility**
   - Icons adopt the current accent color and support light/dark variants automatically.
   - Provide hover tooltips: “Text Color” for the font icon and “Background Color” for the background icon.
   - Enforce a readable contrast ratio (≥ 4.5:1) between text and background. Show a visual warning badge if the chosen colors fail this check.
   - Settings remain persistent across reloads, rehydrated from `localStorage`.

## Agent Collaboration Notes
- Before drafting implementation plans, run `@glm discuss` and `@codex discuss` sessions to capture design input.
- Summaries from those discussions should link back to this document when logging decisions.
- GLM discussions now call the live `glm-4.6` model through the Z.AI SDK. Ensure `zai-sdk` is installed, set `ZAI_API_KEY`, and flip `"enable_live_discuss": true` for the `glm` agent before running these sessions.
