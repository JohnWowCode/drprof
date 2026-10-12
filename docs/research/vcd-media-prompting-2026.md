# Research brief: media prompting vocabulary (October 2026)

For: *The Vibe Coder's Dictionary*, the chapters on directing AI tools to make images, video, game art, music, sound effects and voices.

Compiled: 2026-10-12. Every "seen" date below is 2026-10-12 unless stated.

## How this was verified (read first)

- **Method.** About 36 web searches. Direct page fetching (WebFetch and curl) was blocked by the session's network policy for every host tried (docs.midjourney.com, developers.openai.com, en.wikipedia.org), so each fact below was checked against the search engine's extracts and quotes of the cited page, not a full read of it. Before print, a human should open each official URL and confirm the quoted wording.
- **Status labels used on every entry:**
  - **[Official]** The claim appears in the tool maker's own docs, help center, blog or support page (as extracted by search).
  - **[Secondary]** Confirmed only by a third-party guide, partner docs, vendor blog or forum. Usable, but cite carefully.
  - **[Craft]** Standard industry vocabulary (film, photo, audio, game art). Definitions are textbook-standard; no single page was fetched for them this session.
  - **[Unverified]** Conflicting or unconfirmed. Do not print as fact without checking.
- **Tool versions move fast.** Any version number, default, range or limit here is a snapshot as of the seen date.

---

## 1. Image prompting

### 1.1 Prompt structure (the "slots")
- **Definition:** A text-to-image prompt is easiest to control when it fills distinct slots: subject (who/what), action or pose, setting/context, medium or style, composition/framing, camera and lens, lighting, color palette, mood, and output format (aspect ratio, resolution). Google's Imagen guide groups these into three top-level parts: subject, context, and style, and says prompts do not need to be long, but good ones are descriptive and clear.
- **Example:** `A red fox (subject) curled asleep on a mossy log (action, setting), watercolor illustration (medium), centered with empty space above (composition), soft overcast light (lighting), muted greens and rust (color), calm and quiet (mood). Aspect 3:2.`
- **Source:** https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide (seen 2026-10-12) **[Official]** for subject/context/style. The full slot list is **[Craft]**.
- **Caveats:** Natural-language models (OpenAI GPT Image, Gemini image models, FLUX.2) do better with sentences than with comma-separated keyword piles; keyword lists are a habit from older Stable Diffusion workflows. Aspect ratio is usually a setting or parameter, not prompt text (Midjourney `--ar 16:9`; OpenAI `size`).

### 1.2 Medium and style descriptors
- **Definition:** Words naming the art form (oil painting, 35mm film photo, cel-shaded 3D, pixel art, vector flat illustration, gouache, isometric diorama) that set rendering technique more strongly than adjectives like "beautiful".
- **Example:** `flat vector illustration, 2px uniform outlines, no gradients`
- **Source:** https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide (style is one of the three guide parts) **[Official]**; specific word list **[Craft]**.
- **Caveats:** Naming living artists as a style shortcut raises ethical and sometimes policy issues; describe the visual traits instead.

### 1.3 Negative prompts (and which tools still use them)
- **Definition:** A separate list of things to exclude, as opposed to describing them in the main prompt.
- **Example:** Midjourney: `cozy reading nook --no people, text`. Stability API: `negative_prompt: "blurry, watermark"`.
- **Sources and status by tool (seen 2026-10-12):**
  - **Midjourney** keeps `--no`. Docs say `--no` equals weighting that part of a multi-prompt at -0.5, and that moderation reads each word after `--no` separately, so `--no modern clothing` is read as "no modern" and "no clothing". https://docs.midjourney.com/docs/no **[Official]**
  - **Stability AI (SD 3.5 API)** has an optional `negative_prompt` string. https://docs.comfy.org/ja/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-diffusion-3-5-image **[Secondary]** (ComfyUI docs for the Stability API node).
  - **Google Imagen on Vertex AI** documents a `negativePrompt` request parameter with examples such as "blurry". https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/omit-content-using-a-negative-prompt **[Official]**. Which Imagen versions still honor it: **[Unverified]**.
  - **Runway Gen-4** says negative phrasing "is not supported and may produce unpredictable or even opposite results". https://help.runwayml.com/hc/en-us/articles/39789879462419 **[Official]**
  - **FLUX.2 (Black Forest Labs)** reportedly has no negative prompt; guides say to describe what you want instead. https://www.atlabs.ai/blog/flux-2-prompting-guide **[Secondary]**; not confirmed on docs.bfl.ai.
  - **OpenAI GPT Image** has no negative-prompt parameter in the image API as far as the docs extracts show; exclusions go in plain language. **[Unverified]**
  - **Kling** listed as having a native negative prompt field by a third-party FAQ. https://invideo.io/faq/how-do-negative-prompts-work-in-ai-video-generation-and/ **[Secondary]**
- **Caveats:** In conversational models, writing "no X" in the main prompt can plant X (the word is now in context). Prefer stating the positive: "empty street" rather than "no people".

### 1.4 Seed
- **Definition:** The integer that initializes the random noise a diffusion model starts from. Same model + same prompt + same settings + same seed gives the same or very similar image, which lets you change one variable at a time.
- **Example:** Midjourney `--seed 1234`; Stability API `seed: 1234`.
- **Sources:** Midjourney seed range 0 to 4294967295 and "similar" results with the same seed and prompt: https://www.asla.org/news-insights/the-field/text-prompting-part-3-a-deep-dive-into-advanced-parameters-in-midjourney **[Secondary]**. Stability SD 3.5 API node: seed integer, default 0, max 4294967294: https://docs.comfy.org/ja/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-diffusion-3-5-image **[Secondary]**.
- **Caveats:** Seeds are not portable across models or versions. Many hosted chat-style generators (ChatGPT, Gemini app) do not expose a seed at all; reproducibility there comes from reference images and edits instead.

### 1.5 Reference images: style, character, object
- **Definition:** Uploading an image so the model copies an aspect of it. *Style reference* copies look (palette, texture, rendering). *Character or omni reference* copies identity of a person, creature, object or vehicle. *Image prompt* copies overall composition and content.
- **Example:** `knight resting by a campfire --oref [url] --ow 100 --sref [url]`
- **Sources (Midjourney):**
  - Omni Reference (`--oref`) puts "characters, objects, vehicles, or non-human creatures" from a reference into new images; compatible with V7; costs 2x GPU time; not compatible with Vary Region, Pan or Zoom Out. https://docs.midjourney.com/hc/en-us/articles/36285124473997 **[Official]**. `--ow` (omni weight) default 100: **[Secondary]**.
  - Character Reference (`--cref`) is the V6 tool; docs say on V7 use Omni Reference instead. https://docs.midjourney.com/docs/character-reference **[Official]**
  - Style Reference (`--sref`): `--sv 6` is the default style-reference version; `--sv 4` is the older V7 sref model (before 16 June 2025). https://docs.midjourney.com/docs/style-reference **[Official]**
  - Midjourney's default model moved V7 to V8.1 on 10 June 2026 and to V8.2 on 24 July 2026: https://updates.midjourney.com/v8-1-is-now-the-default-model **[Official]** for V8.1; V8.2 date **[Secondary]** (https://medium.com/@inchristiely/midjourney-v8-2-is-now-the-default-five-things-that-changed-30c8dffcc492). Whether `--oref` works on V8.x: **[Unverified]**.
- **Other tools:** Veo 3.1 "ingredients to video" accepts up to 3 reference images of a character, object or scene (https://developers.googleblog.com/en/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/ **[Official]**). OpenAI's cookbook lists character consistency and identity preservation in edits as GPT Image capabilities (https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide **[Official]**); the "up to 16 reference images" figure is **[Secondary/Unverified]**.
- **Caveats:** Reference strength is a dial; too high copies the pose and background too, too low drifts identity.

### 1.6 Inpainting
- **Definition:** Regenerating only a masked region of an existing image while keeping the rest.
- **Example:** Mask the sky, prompt `stormy purple sky with lightning, same lighting direction on the castle`.
- **Source:** OpenAI edits: the mask is "an additional image whose fully transparent areas (e.g. where alpha is zero) indicate where image should be edited"; image and mask must share format and size (under 50 MB) and the mask needs an alpha channel. https://developers.openai.com/api/docs/guides/image-generation and https://developers.openai.com/api/reference/python/resources/images/methods/edit **[Official]**. Midjourney's equivalent is Vary Region **[Official]** (named on the Omni Reference page).
- **Caveats:** A white-on-black mask is fully opaque, so the API may return the image unchanged with no error (https://www.adpicto.com/en/blog/gpt-image-2-image-editing-workflow **[Secondary]**). OpenAI GPT Image models may treat the mask as guidance rather than a hard boundary **[Unverified]**.

### 1.7 Outpainting
- **Definition:** Extending an image beyond its original borders, generating new content that continues the scene.
- **Example:** Midjourney Zoom Out or Pan; Higgsfield `outpaint_image`; prompt `continue the forest to the left, same fog and time of day`.
- **Source:** Midjourney Pan and Zoom Out named in the Omni Reference doc above **[Official]**. General definition **[Craft]**.
- **Caveats:** Seams and lighting mismatches appear at the original edge; restate lighting and time of day.

### 1.8 Upscaling
- **Definition:** Increasing pixel resolution, either plainly (interpolation) or generatively (the model invents fine detail). "Subtle" vs "creative" upscale modes trade fidelity for added detail.
- **Example:** Generate at 1024x1024, then upscale 2x for a 2048 print.
- **Source:** **[Craft]**. Native high resolution is now common: OpenAI's guide lists sizes up to 3840x2160 and 2160x3840 for its newest model (gpt-image-2), while GPT Image 1.5 is limited to 1024x1024, 1024x1536, 1536x1024 or auto. https://developers.openai.com/api/docs/guides/image-generation **[Official]**. Gemini 3 Pro Image (preview) up to 4K; Gemini 2.5 Flash Image at 1024px. https://ai.google.dev/gemini-api/docs/image-generation **[Official]**.
- **Caveats:** Never upscale pixel art with smoothing filters; use nearest-neighbor integer scaling (see 4.4). Creative upscalers can change faces and text.

### 1.9 Text rendering in images
- **Definition:** Getting legible, correctly spelled words (signs, logos, UI labels, posters) inside a generated image.
- **Example:** `A neon sign that reads "NIGHT OWL CAFE" exactly, in rounded pink letters. Render the quoted text verbatim.`
- **Sources:** OpenAI's prompting guide lists reliable text rendering with crisp lettering and consistent layout as a capability: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide **[Official]**. Gemini 3 Pro Image is described as rendering "high-fidelity text" for logos, diagrams and posters: https://ai.google.dev/gemini-api/docs/image-generation **[Official]**. Put the exact string in quotes, add a "verbatim" instruction, spell unusual words letter by letter: https://runware.ai/docs/models/openai-gpt-image-2/guides/prompting.md **[Secondary]**. FLUX.2 accepts hex color codes for text and brand colors: https://docs.together.ai/docs/quickstart-flux-2 **[Secondary]**.
- **Caveats:** Long paragraphs still fail more than short labels. For shipping UI, render text in code or a design tool and generate only the art.

### 1.10 Structured (JSON) prompts
- **Definition:** Writing the prompt as JSON fields (scene, subjects, style, palette, lighting, camera) so each slot is explicit and editable.
- **Example:** `{"subject":"brass robot","style":"studio product photo","palette":["#1E2A38","#E3A857"],"lighting":"softbox key from left","camera":"85mm, f/2.8"}`
- **Source:** Together AI says FLUX.2 "is trained to understand structured JSON prompts": https://docs.together.ai/docs/quickstart-flux-2 **[Secondary]** (partner docs).
- **Caveats:** Not every model benefits; for others JSON is just text. Useful for templating a consistent set.

### 1.11 Weights and multi-prompts
- **Definition:** Splitting a prompt into parts and assigning relative importance.
- **Example:** Midjourney `space::2 ship::1` (more "space" than "ship").
- **Source:** https://docs.midjourney.com/docs/no (negative weight equivalence) **[Official]**; weight arithmetic and "sum must be positive" **[Secondary]** (https://aituts.com/midjourney-prompt-weights/).
- **Caveats:** Weight syntax is tool-specific; `::` means nothing to OpenAI or Gemini.

### 1.12 Seamless / tileable output
- **Definition:** An image whose left/right and top/bottom edges match so it repeats without visible seams.
- **Example:** `cobblestone path texture, top-down, even lighting --tile`
- **Source:** Midjourney `--tile` makes edges line up with copies of itself and generates a single tile; page references V8.1. https://docs.midjourney.com/docs/tile **[Official]**
- **Caveats:** Check by tiling 3x3 in an editor. See 4.9.

### 1.13 Transparent background
- **Definition:** Output with an alpha channel so the subject can be placed over any background (sprites, icons, stickers).
- **Example:** OpenAI `background: "transparent"`, `output_format: "png"`.
- **Source:** "When using transparent, set the output format to png or webp"; transparent backgrounds are "available in preview for gpt-image-2". https://developers.openai.com/api/docs/guides/image-generation **[Official]**
- **Caveats:** Many generators cannot produce real alpha; asking for "transparent background" yields a checkerboard pattern painted into the pixels. Use a background-removal step instead.

### 1.14 Consistency across a set
- **Definition:** Making many images (a cast, an icon set, a storyboard) look like one family: same character identity, palette, line weight, lighting and camera height.
- **Example fragment (style lock):** `Same style as previous: thick 3px black outline, flat cel shading, palette #2B2D42 #8D99AE #EF233C, light from top-left, 3/4 view.`
- **Sources:** Reference images (1.5); Gemini's guide recommends multi-turn conversation to "progressively refine your image": https://ai.google.dev/gemini-api/docs/image-generation **[Official]**; seeds (1.4).
- **Caveats:** Keep a written "style bible" prompt block and paste it unchanged into every request; change only the subject line. Generate the hero asset first, then use it as the reference for the rest.

---

## 2. Photography and cinematography vocabulary

All definitions in this section are standard film/photo terms **[Craft]** unless a source is given. Generators that publicly say they respond to these terms: Imagen's guide covers camera proximity, position, lighting, camera settings, lens types and film types (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide **[Official]**, section detail via https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/photography-modifiers-in-ai-generated-images **[Secondary]**). Veo responds to "eye level, high angle, worms eye, dolly shot, zoom shot, pan shot, tracking shot" (https://replicate.com/blog/using-and-prompting-veo-3 **[Secondary]**).

### 2.1 Shot sizes (tightest to widest)
StudioBinder's standard list and abbreviations: ECU, CU, MCU, MS, CS (cowboy), MFS, FS, WS, EWS (aka extreme long shot). https://www.studiobinder.com/blog/types-of-camera-shot-sizes-in-film/ (seen 2026-10-12) **[Secondary]** (industry standard reference).

| Term | Definition | Prompt fragment |
|---|---|---|
| Extreme close-up (ECU) | One feature fills the frame (an eye, a key in a lock). | `extreme close-up of her eye, iris detail` |
| Close-up (CU) | Face fills the frame, top of head to chin. | `close-up portrait` |
| Medium close-up (MCU) | Head and shoulders to mid-chest. | `medium close-up, chest up` |
| Medium shot (MS) | Waist up. | `medium shot, waist up` |
| Cowboy shot (CS) | Mid-thigh up (originally to show a holstered gun). | `cowboy shot, hand near holster` |
| Medium full shot (MFS) | Knees up. | `medium full shot` |
| Full shot (FS) | Whole body, head to feet, little surroundings. | `full-body shot, feet visible` |
| Wide shot (WS) | Subject small within the location. | `wide shot of the knight in the courtyard` |
| Extreme wide shot (EWS) | Landscape dominates; subject tiny or absent. Often the establishing shot. | `extreme wide establishing shot` |

Caveat: generators often crop feet or heads at full-shot sizes; say `feet visible` or `full body, head to toe` explicitly.

### 2.2 Camera angles
- **Eye level:** Camera at subject's eye height; neutral. `eye-level shot`
- **Low angle:** Camera below looking up; subject feels powerful. `low-angle shot looking up at the giant`
- **Worm's-eye view:** Extreme low angle, from the ground. `worm's-eye view`
- **High angle:** Camera above looking down; subject feels small or vulnerable. `high-angle shot`
- **Overhead / bird's-eye / top-down:** Camera directly above, lens pointing down. StudioBinder pairs overhead with "omniscience". https://www.studiobinder.com/blog/types-of-camera-shots-angles-in-film/ **[Secondary]**. `top-down overhead shot of the chessboard`
- **Dutch angle (Dutch tilt, canted angle):** Camera rolled on its lens axis so the horizon is tilted; signals unease. `Dutch angle, horizon tilted 20 degrees` **[Craft]**
- **Over-the-shoulder (OTS):** Framed past one character's shoulder at another. `over-the-shoulder shot`
- **POV:** What a character sees. `first-person POV, hands visible`
- Caveat: "top-down" for game art means orthographic map view, which is a different request from a cinematic overhead photo; see 4.6.

### 2.3 Lenses and focal length
- **Focal length:** Distance (mm) that sets field of view on a given sensor. On full-frame: ultra-wide 14 to 24mm, wide 24 to 35mm, normal around 50mm, short telephoto 85 to 135mm (classic portrait), telephoto 200mm+. **[Craft]**
- **Effects:** Wide lenses expand field of view and exaggerate perspective (big noses at close range); telephoto lenses compress perspective so background looks closer and larger. https://samples.technavio.com/?p=13252 **[Secondary]**
- **Fisheye:** Ultra-wide (often 8 to 16mm) with strong barrel distortion. **[Secondary]** (https://prompt-architects.com/blog/226-camera-and-lens-terms-that-change-your-ai-images)
- **Macro:** Close focusing at 1:1 magnification or greater; insects, jewelry, textures. **[Secondary]** (same source)
- **Example:** `85mm portrait lens, f/1.8, shallow depth of field`
- **Caveat:** Generators treat lens names as style cues; they do not compute real optics. A third-party summary of the Imagen guide notes it does not claim images follow real exposure math **[Secondary]**.

### 2.4 Depth of field, aperture, bokeh
- **Depth of field (DoF):** The front-to-back range that looks sharp. **Shallow DoF** isolates a subject against a blurred background; **deep DoF** keeps everything sharp (landscapes, architecture). **[Craft]**
- **Aperture (f-stop):** Lens opening; lower f-numbers (f/1.4, f/2) give shallower DoF; higher (f/8, f/16) deeper. **[Craft]**
- **Bokeh:** The quality of out-of-focus blur, especially round highlight discs. Imagen guide lists bokeh and soft focus as modifiers **[Secondary]**.
- **Example:** `shallow depth of field, creamy bokeh of city lights behind her`
- **Caveat:** For game sprites and UI assets you usually want the opposite: everything in focus, no blur.

### 2.5 Lighting setups
- **Three-point lighting:** Key (main light, sets exposure and mood), fill (softens the key's shadows), backlight/rim/hair light (separates subject from background, usually dimmer than the key). https://petapixel.com/2018/08/03/heres-an-intro-to-three-point-lighting-for-portraits **[Secondary]**. `three-point lighting, soft fill, strong rim light`
- **Key / fill / rim:** As above. **Key-to-fill ratio** (e.g. 2:1 bright, 8:1 dramatic) controls contrast **[Craft]**; one source suggests fill one or two stops below key, or no fill for a darker look **[Secondary]**.
- **Rembrandt lighting:** Key about 45 degrees to one side and slightly above eye level, leaving a small triangle of light on the shadow-side cheek under the eye. https://www.slrlounge.com/glossary/rembrandt-lighting-definition/ **[Secondary]**. `Rembrandt lighting, triangle of light on the left cheek`
- **Butterfly / paramount:** Key high and centered in front, making a small butterfly-shaped shadow under the nose. **[Craft]**
- **Split lighting:** Key at 90 degrees; half the face lit, half dark. **[Craft]**
- **Chiaroscuro:** Strong light/dark contrast with deep shadows (from Renaissance painting, e.g. Caravaggio). `chiaroscuro, single candle, deep black shadows` **[Craft]**
- **Low-key / high-key:** Low-key is mostly dark with strong contrast (noir, horror); high-key is bright with soft, minimal shadows (comedy, product, medical). **[Craft]**
- **Golden hour:** Shortly after sunrise or before sunset; warm, low, soft, long shadows. **Blue hour:** Just before sunrise or after sunset; cool, even, deep blue sky. **[Craft]**
- **Practical light:** A light source visible in the scene (lamp, neon sign, screen). **Motivated lighting:** Light that appears to come from a source in the world. **[Craft]**
- **Hard vs soft light:** Small or distant source gives hard, crisp shadows; large or diffused source gives soft shadows. **[Craft]**
- **Volumetric light / god rays:** Visible light beams through haze or dust. **[Craft]**

### 2.6 Color grading terms
- **Color correction vs grading:** Correction fixes technical problems (white balance, exposure, matching shots); grading sets the creative look. **[Craft]**
- **LUT (look-up table):** A preset that maps input colors to output colors to apply a look. Nikon describes a LUT that recreates teal and orange with "reddish highlights and bluish shadows". https://imaging.nikon.com/imaging/support/digitutor/z_8/techniques/202505_62_01_ml.html **[Official]** (Nikon).
- **Teal and orange:** Cool shadows/backgrounds, warm skin tones; blockbuster look. **[Secondary]**
- **Bleach bypass:** From a film process (silver retention) that gives high contrast and low saturation. Same Nikon page **[Official]**.
- **Log footage:** Flat, low-contrast camera recording that preserves dynamic range for grading. **[Craft]**
- **Other prompt-useful words:** desaturated, crushed blacks, lifted blacks (faded/matte), warm/cool white balance, monochrome, sepia, split-toning, film grain, halation, Kodachrome-style, high contrast. **[Craft]**
- **Example:** `teal-and-orange grade, lifted blacks, subtle film grain`
- **Caveat:** Film-stock names (Kodak Portra 400, Cinestill 800T) work as style cues, but the model is imitating what photos tagged with those words looked like, not emulating the chemistry.

---

## 3. Video generation prompting

### 3.1 Prompt structure for video
- **Definition:** Video prompts add *time* to an image prompt: what moves, how the camera moves, and in what order. A common order is shot/camera first, then subject and action, then setting, style, and (for audio-capable models) sound.
- **Example:** `Slow dolly-in, eye level, 35mm. A lighthouse keeper climbs the spiral stairs carrying a lantern. Rain streaks the windows. Muted blue grade. Audio: rain on glass, distant foghorn, his footsteps on iron.`
- **Sources:** Google's Veo 3.1 prompting guide (framework for directing the model): https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1 **[Official]** (only the intro was visible in extracts). Camera-first ordering and naming lens and move explicitly: https://medium.com/@miguelivanov/mastering-veo-3-an-expert-guide-to-optimal-prompt-structure-and-cinematic-camera-control-693d01ae9f8b **[Secondary]**. Write camera movement as its own sentence: https://leonardo.ai/news/mastering-prompts-for-veo-3 **[Secondary]**.
- **Caveat:** One action per clip works far better than a sequence of five events in eight seconds.

### 3.2 Image-to-video: describe motion, not the picture
- **Definition:** When you supply a starting image, the image already defines composition, subject, lighting and style; the prompt should describe only what happens next.
- **Example:** `The steam rises slowly from the cup; the camera pushes in gently.` (not "a cup of coffee on a wooden table")
- **Source:** Runway's Image to Video guide (optimized for Gen-4.5): "your image defines composition, subject matter, lighting, and style... Your prompt's role is to describe what should happen". https://help.runwayml.com/hc/en-us/articles/48324313115155 **[Official]**
- **Caveats:** If the image contains motion cues (dust, motion blur) and you ask for a still subject, the two conflict (same source).

### 3.3 Positive phrasing for camera and motion
- **Definition:** State what should happen instead of what should not.
- **Example:** `Locked camera. The camera remains still.` rather than `no camera movement`.
- **Source:** Runway Gen-4 prompting guide, which says negative phrasing is not supported. https://help.runwayml.com/hc/en-us/articles/39789879462419 **[Official]**
- **Caveat:** Applies to most video models, not just Runway.

### 3.4 Camera movements
Definitions **[Craft]**. Tool support noted where verified.

| Move | Definition | Fragment |
|---|---|---|
| Static / locked-off | Camera does not move. | `locked-off tripod shot` |
| Pan | Camera rotates left/right on a fixed point. | `slow pan left across the skyline` |
| Tilt | Camera rotates up/down on a fixed point. | `tilt up from boots to face` |
| Roll | Camera rotates around the lens axis. | `slow clockwise roll` |
| Dolly in/out (push-in, pull-out) | Camera physically moves toward/away from subject. | `slow push-in on her face` |
| Truck (track) left/right | Camera physically moves sideways, parallel to subject. | `truck right alongside the runner` |
| Pedestal / boom | Camera moves straight up/down without tilting. | `pedestal up to reveal the city` |
| Crane / jib | Camera rises or descends on an arm, often sweeping. | `crane up and back to a wide shot` |
| Orbit / arc | Camera circles the subject. | `360-degree orbit around the statue` |
| Tracking / follow | Camera follows a moving subject. | `tracking shot behind the cyclist` |
| Handheld | Slight organic shake, documentary feel. | `handheld, subtle shake` |
| Zoom | Lens focal length changes; camera does not move. | `slow zoom in` |
| Dolly zoom (vertigo effect) | Dolly one way while zooming the other; background warps, subject stays same size. | `dolly zoom, background stretches` |
| Crash zoom | Very fast zoom in. | `crash zoom onto the alarm clock` |
| FPV drone | Fast, swooping first-person drone flight. | `FPV drone dive through the canyon` |
| Whip pan | Very fast pan that blurs, often a transition. | `whip pan to the doorway` |

- **Kling** official camera control: "six basic camera movements... horizontal, vertical, zoom, pan, tilt, roll" plus four "Master Shots". https://kling.ai/quickstart/ai-camera-control-guide **[Official]**
- **Higgsfield** presets include crash zoom, dolly in, bullet time, FPV drone (WAN 2.5 camera control guide): https://higgsfield.ai/blog/WAN-AI-Camera-Control-Your-Guide-to-Cinematic-Motion **[Official]** (Higgsfield blog). Dolly zoom in/out presets: https://geo.higgsfield.ai/blog/crane-shot-dolly-zoom-presets-ai-video-generation **[Secondary]**. Higgsfield Cinema Studio exposes genre, lighting, lens, focal length, aperture and move-set controls; options differ by version: https://www.seedance.tv/blog/higgsfield-cinema-studio-camera-settings **[Secondary]**.
- **Caveat:** Models confuse dolly and zoom. If you want physical movement, say `the camera physically moves forward, no zoom`.

### 3.5 Pacing and shot length
- **Definition:** Pacing is how fast things happen within a clip and how often you cut. Generators produce short clips, so pacing is controlled by speed words (slow, gradual, sudden) and by cutting clips together in an editor.
- **Example:** `In slow motion, over the full shot, the petals fall.`
- **Sources:** Kling 3.0 clips 3 to 15 seconds with up to multi-shot output: https://higgsfield.ai/blog/Kling-3.0-is-on-Higgsfield-User-Guide-AI-Video-Generation and https://www.atlascloud.ai/blog/tips/kling-4-controlled-camera-movement **[Secondary]**. Veo clips around 8 seconds (forum and guide examples use `durationSeconds: 8`): **[Secondary]**. Veo's other allowed durations: **[Unverified]**.
- **Caveat:** Runway suggests adding `continuous, seamless shot` if the model inserts unwanted cuts (https://help.runwayml.com/hc/en-us/articles/48324313115155 **[Official]**).

### 3.6 Frame rate
- **Definition:** Frames per second. 24 fps is the film standard (motion blur, "cinematic"), 30 fps common for web/TV, 60 fps for smooth game footage and sports. Slow motion is shot at a high rate and played back at a lower one. **[Craft]**
- **Example:** `cinematic 24fps look, natural motion blur`
- **Source:** **[Craft]**. Native output frame rates of specific generators (Veo, Kling, Runway) were not confirmed this session **[Unverified]**.
- **Caveat:** Asking for "60fps" in a prompt rarely changes the output frame rate; it is a model setting or a post-process (frame interpolation).

### 3.7 Start frame and end frame (keyframes)
- **Definition:** Supplying the first image, the last image, or both, so the model generates the motion between them. Useful for transitions, loops (same start and end frame), and matching cuts.
- **Example:** Start: character standing; end: character mid-jump. Prompt: `she crouches and leaps toward the camera`.
- **Sources:** Veo 3.1 "first and last frame" (Gemini API fields `image` and `lastFrame`): https://developers.googleblog.com/en/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/ **[Official]** for the feature; field names via https://dev.to/_37bbf0c253c0b3edec531e/how-to-use-veo-31-api-4f3h **[Secondary]**. Kling 3.0 start/end frames, end-frame-only supported: https://higgsfield.ai/blog/Kling-3.0-is-on-Higgsfield-User-Guide-AI-Video-Generation **[Secondary]**.
- **Caveat:** Start and end frames that differ too much (new location, new outfit) produce morphing. For a game-menu background loop, use the same image as start and end.

### 3.8 Scene extension
- **Definition:** Continuing an existing clip by generating new footage from its final moments.
- **Source:** Veo 3.1 extension generates each new video "based on the final second of the previous clip". https://developers.googleblog.com/en/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/ **[Official]**. "7 seconds per extension, up to 20 times": **[Secondary/Unverified]**.
- **Caveat:** Drift accumulates; re-anchor with a reference image.

### 3.9 Motion control (motion transfer)
- **Definition:** Taking the movement from a reference video (a dance, a fight move, your own acting) and applying it to a character image.
- **Example:** Upload your webcam clip of a wave plus a cartoon fox image; the fox waves.
- **Sources:** Kling Motion Control transfers a reference video's movement onto a character image; you can choose whether camera follows the reference or the image framing: https://studio.aifilms.ai/blog/kling-3-motion-control-tutorial **[Secondary]**. Higgsfield offers Kling motion control as a single-character recast tool (per the Higgsfield connector available in this research session; no public doc page retrieved) **[Unverified]**.
- **Caveat:** Body proportions that differ a lot between reference and character cause limb glitches.

### 3.10 Consistency across shots
- **Definition:** Keeping characters, wardrobe, location and look stable across separate clips.
- **Techniques:** Reference images ("ingredients", up to 3 in Veo 3.1), reusing the same start frame, a fixed style block in every prompt, and a shared cast in multi-shot tools (Higgsfield Cinema Studio 4.0 emphasizes "shared cast references" **[Secondary]**).
- **Source:** Veo blog above **[Official]**; reference-image support was reported as inconsistent across endpoints at one point (https://discuss.ai.google.dev/t/veo-3-1-reference-images-docs-say-available-api-says-not-supported/111853 **[Secondary]**).
- **Caveat:** Generate key stills first, approve them, then animate from them.

### 3.11 Native audio in video prompts
- **Definition:** Some video models (Veo 3 and later, Kling 3.0) generate synchronized dialogue, sound effects and ambience from the prompt.
- **Example:** `He says: "We're not alone." Sound: wind howling, a metal door creaks behind him. No music.`
- **Sources:** Keep dialogue short (fits one breath in ~8 s), separate sentences for audio cues, spell names phonetically if mispronounced: https://replicate.com/blog/using-and-prompting-veo-3 **[Secondary]**. Suggested order: dialogue, SFX tied to visible actions, ambience, then audio exclusions: https://www.veo3ai.io/blog/veo-3-native-audio-prompt-guide-2026 **[Secondary]**. Kling 3.0 native audio: **[Secondary]**.
- **Caveat:** For a game, generate SFX and music separately (Section 5) so you can mix and loop them; baked-in video audio is hard to edit.

---

## 4. Game art terms

Definitions are standard game-development vocabulary **[Craft]** unless a source is given.

### 4.1 Sprite
- **Definition:** A 2D image used as a game object (character, item, projectile), usually with a transparent background.
- **Example:** `single game sprite of a slime enemy, side view, transparent background, centered, no shadow`
- **Caveat:** Ask for one sprite per image when you need clean edges; generators add ground shadows and backgrounds by default.

### 4.2 Sprite sheet
- **Definition:** One image containing many frames or sprites laid out on a regular grid (for animation) or packed together (for many assets). Each frame occupies a fixed cell, e.g. 8 frames of 64x64 in a row.
- **Example:** `sprite sheet, 8-frame walk cycle, side view, each frame 64x64 on a uniform grid, same character in every frame`
- **Caveat:** Image generators rarely keep perfect grid alignment or identical proportions frame to frame. Expect to fix in an editor (Aseprite) or generate frames from a reference.

### 4.3 Tileset and tilemap
- **Definition:** A tileset is a grid of small, same-size tiles (16x16, 32x32) that snap together to build levels; a tilemap is the level built from them. **Autotiles** include edge and corner variants so terrain joins automatically.
- **Example:** `top-down 16x16 grass and dirt tileset with edge and corner transitions, pixel art`
- **Caveat:** Edges must match pixel-perfectly; AI output usually needs cleanup.

### 4.4 Pixel art resolution and palettes
- **Definition:** Pixel art is made at a low native resolution where each pixel is placed deliberately, then scaled up by whole-number factors (2x, 3x, 4x) with nearest-neighbor filtering so pixels stay square and crisp. A **limited palette** (e.g. 4, 16 or 32 colors) gives coherence.
- **Example:** `pixel art at native 64x64, 16-color palette, no anti-aliasing, no dithering on the outline`
- **Source:** PICO-8, a common reference point: 128x128 screen, fixed 16-color palette, 8x8 sprites. https://www.lexaloffle.com/pico-8.php **[Official]**. Lospec palette list (https://lospec.com/palette-list) as a palette library: **[Unverified]** this session.
- **Caveats:** Most image models produce "pixel-art style" images at 1024px with inconsistent pixel sizes and stray colors. Downscale to the true grid and quantize to the palette afterward. Never use bilinear filtering on pixel art in the engine.

### 4.5 Isometric
- **Definition:** A projection where the three axes appear equally foreshortened; in games, usually "2:1 dimetric" pixel art where lines go 2 pixels across per 1 up (about 26.57 degrees), with no vanishing point.
- **Example:** `isometric game tile of a small cottage, 2:1 isometric, no perspective, transparent background`
- **Caveat:** Generators often add perspective; say `no vanishing point, orthographic isometric`.

### 4.6 Orthographic (vs perspective)
- **Definition:** A projection with no perspective: parallel lines stay parallel and objects do not shrink with distance. Used for top-down maps, side-scrollers, and technical views (front/side/back character turnarounds).
- **Example:** `orthographic top-down view, no perspective distortion`
- **Caveat:** "Top-down" alone may give a dramatic overhead photo; add `orthographic`.

### 4.7 UI icon sets
- **Definition:** A family of icons sharing grid size (e.g. 24x24 or 64x64), stroke width, corner radius, perspective, lighting direction and palette.
- **Example:** `game inventory icon set: sword, shield, potion, key; same 3/4 angle, same light from top-left, 2px dark outline, consistent palette, each on its own transparent tile`
- **Caveat:** Generate one icon first, approve it, then use it as a style reference for the rest (1.5, 1.14).

### 4.8 9-slice (nine-slice) sprites
- **Definition:** A UI image divided by four guide lines into nine regions: corners stay fixed size, edges stretch or tile in one direction, and the center stretches or tiles in both, so one panel or button image scales to any size without distorting its corners.
- **Example:** `fantasy UI panel frame with ornate corners and plain straight edges, flat center, designed for 9-slice scaling`
- **Source:** Unity: set Mesh Type to Full Rect, set borders (L/R/T/B) in the Sprite Editor, then set Draw Mode to Sliced or Tiled; Tight mesh can break 9-slicing. https://docs.unity.com/en-us/engine/6000.3/manual/unity2d/sprite/9-slice/set-sprite-9slicing.md **[Official]**
- **Caveat:** Decorations in the middle of an edge will stretch; keep ornaments in the corners.

### 4.9 Texture atlas
- **Definition:** Many small textures packed into one large image, with coordinates for each. Fewer texture switches means fewer draw calls and better performance.
- **Source:** Unity Sprite Atlas batching benefit: https://www.codeandweb.com/texturepacker/tutorials/using-spritesheets-with-unity **[Secondary]** (vendor). Official Unity Sprite Atlas page not retrieved **[Unverified]**.
- **Caveat:** Atlas packing is a build step (engine or TexturePacker), not something to ask an image model for.

### 4.10 Seamless / tileable textures
- **Definition:** A texture that repeats across a surface with no visible edge, used for floors, walls, terrain, skyboxes.
- **Example:** `seamless tileable stone wall texture, flat even lighting, no shadows from a single direction, no perspective, square`
- **Source:** Midjourney `--tile` **[Official]** (1.12).
- **Caveat:** Baked-in directional shadows and unique features (one big crack) make repetition obvious. Ask for even lighting and uniform detail.

### 4.11 PBR texture maps
- **Definition:** Physically based rendering uses several aligned maps per material:
  - **Base color (albedo):** surface color without lighting or shadows.
  - **Metallic:** grayscale; black is non-metal, white is metal.
  - **Roughness:** grayscale; white is rough (blurry reflections), black is smooth (sharp reflections).
  - **Normal map:** RGB-encoded surface direction that fakes small bumps.
  - **Height / displacement:** grayscale depth.
  - **Ambient occlusion (AO):** grayscale contact shadowing in crevices.
- **Sources:** Base color and metalness definitions: https://help.sketchfab.com/en/articles/16152630-pbr-maps **[Secondary]** (Sketchfab docs). Roughness white = rough: https://docs.unity3d.com/550/Documentation/ScriptReference/ProceduralOutputType.Roughness.html **[Official]** (legacy Unity). Channel packing AO=R, roughness=G, metallic=B ("ORM"): https://help.shapediver.com/doc/metalness-roughness **[Secondary]**, consistent with the glTF 2.0 convention **[Craft]**.
- **Example:** `albedo map only, flat, no baked lighting or shadows, seamless`
- **Caveat:** Image generators produce a "beauty" image with lighting baked in. Ask for flat albedo, then derive normal/roughness with a dedicated material tool.

---

## 5. Audio

### 5.1 Sample rate
- **Definition:** Samples per second of digital audio. 44.1 kHz is the CD/music standard; 48 kHz is the film, video, broadcast and game standard. Higher rates (96 kHz) are used in recording and sound design for pitch-shifting headroom.
- **Example spec:** `Deliver WAV, 48 kHz, 24-bit.`
- **Source:** 48 kHz adopted across film, video and broadcast: https://www.proav.de/audio/samplerates.html **[Secondary]**. 48 kHz as game norm: forum consensus only **[Secondary/weak]**.
- **Caveat:** Mixing files at different sample rates in an engine causes resampling; pick one rate per project.

### 5.2 Bit depth
- **Definition:** Bits per sample, which sets the theoretical noise floor: about 6 dB of dynamic range per bit, so 16-bit about 96 dB and 24-bit about 144 dB (theoretical). 24-bit gives headroom while recording and editing; 16-bit is fine for final delivery.
- **Source:** https://www.proav.de/audio/samplerates.html **[Secondary]**.
- **Caveat:** Real converters fall short of 144 dB; the practical benefit is headroom.

### 5.3 LUFS and loudness targets
- **Definition:** LUFS (Loudness Units relative to Full Scale) measures perceived loudness over time (integrated loudness), per ITU-R BS.1770. Platforms normalize playback to a target, so mastering louder than the target mostly costs dynamics. **True peak (dBTP)** is the inter-sample peak level; keep headroom to avoid clipping after encoding.
- **Targets (seen 2026-10-12):**
  - **Spotify:** -14 LUFS integrated normal mode; limiter at -1 dB; recommends -14 LUFS and true peak at or below -1 dBTP; listener options Loud -11 and Quiet -19. https://support.spotify.com/au/artists/article/loudness-normalization/ **[Official]**
  - **Apple Music (Sound Check):** about -16 LUFS. **[Secondary]** (https://www.roexaudio.com/blog/how-to-master-music-for-streaming-spotify-apple-music-deezer-youtube); whether it turns quiet tracks up is disputed **[Unverified]**.
  - **YouTube:** about -14 LUFS, turns loud audio down, does not boost. **[Secondary]**
  - **Games, console:** -24 LUFS integrated (+/-2 LU), citing PlayStation guidance as of February 2024. **Games, mobile/portable:** -18 LUFS (+/-2 LU), max -1 dBTP, loudness range up to 20 LU. https://audiokinetic.com/ko/blog/mastering-a-game-with-wwise-part1 **[Secondary]** (Audiokinetic is the Wwise maker, citing Sony's ASWG). An older figure of -23 LUFS appears in earlier coverage; measure over at least 30 minutes of gameplay. https://designingsound.org/2013/02/loudness-in-game-audio/ **[Secondary]**. Current Sony document text: **[Unverified]** (behind DevNet).
- **Example:** `Master the menu music to -18 LUFS integrated, true peak -1 dBTP (mobile game).`
- **Caveat:** Game loudness is measured on the whole game mix over a session, not per file. Individual SFX files are not normalized to -24 LUFS.

### 5.4 Dynamic range and loudness range
- **Definition:** Dynamic range is the difference between the quietest and loudest parts; loudness range (LRA, in LU) measures how much loudness varies over a program. Heavy limiting shrinks both (the "loudness war").
- **Source:** LRA limit of 20 for mobile games: Audiokinetic blog above **[Secondary]**. Definition **[Craft]**.
- **Example:** `keep the dynamics: quiet verses, big choruses, no heavy limiting`

### 5.5 EQ (equalization)
- **Definition:** Boosting or cutting frequency bands. Useful words: low-end/sub (below ~60 Hz), bass, low-mids ("mud", ~200 to 500 Hz), mids, presence (~2 to 5 kHz), highs/air (10 kHz+), high-pass/low-cut filter (removes lows), low-pass/high-cut (removes highs), "telephone EQ" (narrow band). **[Craft]**
- **Example:** `voice with a telephone EQ, thin and narrow`; `warm, bass-heavy, rolled-off highs`.

### 5.6 Compression and limiting
- **Definition:** A compressor reduces level above a threshold by a ratio, with attack and release times; makes sound more even and punchy. A limiter is a very high-ratio compressor that prevents peaks past a ceiling. Sidechain compression ducks one sound when another plays (music dips under dialogue; "pumping" in EDM). **[Craft]**
- **Example:** `punchy compressed drums, sidechain pumping on the synth pads`

### 5.7 Reverb and delay
- **Definition:** Reverb simulates a space's reflections (room, hall, plate, spring, cathedral); key parameters are decay time, pre-delay, and wet/dry mix. Delay/echo repeats the sound at intervals. **Dry** means no effect. **[Craft]**
- **Example:** `dry, close-mic'd voice` vs `huge cathedral reverb, long tail`
- **Caveat:** For game SFX, deliver dry and let the engine add reverb per environment.

### 5.8 Stems
- **Definition:** Separate audio files for groups of a mix (drums, bass, melody, vocals, pads) that together sum to the full track. Needed for remixing, adaptive music (5.15) and ducking.
- **Example:** Request or export `drums, bass, lead, pads` stems at the same length and start point.
- **Caveat:** AI stem separation of a finished song can leave artifacts; native stem export (if the generator offers it) is cleaner **[Unverified]** per tool.

### 5.9 Loops and seamless loop points
- **Definition:** A loop is audio designed to repeat. The **loop point** is where playback jumps back; a seamless loop has matching level, phase and musical position at the end and start, with no click (cut at a zero crossing or use a short crossfade). Musical loops should be an exact number of bars at the BPM.
- **Example:** `seamless 8-bar loop at 120 BPM, no intro, no ending, no fade`
- **Source:** ElevenLabs Sound Effects v2 has a `loop` flag (default off): https://www.mintlify.com/elevenlabs/elevenlabs-python/api-reference/audio/sound-effects **[Secondary]** (SDK mirror). Loop definitions **[Craft]**.
- **Caveat:** Most music generators write intros and endings; ask for no intro/outro and trim to bar boundaries yourself. Reverb tails at the end must be wrapped to the start for a truly seamless loop.

### 5.10 BPM, key, time signature
- **Definition:** BPM (beats per minute) is tempo (e.g. 70 ballad, 120 pop/house, 140 dubstep, 170 drum and bass). Key is the tonal center and scale (C major bright, A minor darker). Time signature is beats per bar (4/4 most pop; 3/4 waltz; 6/8 lilting; 7/8 uneven). **[Craft]**
- **Example:** `120 BPM, A minor, 4/4`
- **Source:** Specific descriptors like "120bpm" in the style field give more consistent Suno results than one genre word: https://www.mintlify.com/gcui-art/suno-api/guides/custom-mode **[Secondary]**.
- **Caveat:** Generators treat BPM and key as hints, not guarantees. Measure the result before building loops on it.

### 5.11 Genre and instrumentation vocabulary for music generators
- **Definition:** Music models respond to genre, era, instrumentation, vocal type, mood, production and structure words.
- **Example style field:** `chiptune, 8-bit square-wave lead, triangle bass, noise-channel drums, upbeat, 150 BPM, instrumental`
- **Useful vocab [Craft]:** genres (lo-fi hip hop, synthwave, orchestral, chiptune, ambient, drum and bass, jazz trio, folk); instruments (Rhodes, 808, analog synth pad, pizzicato strings, taiko, solo cello); vocals (female alto, breathy, choir, no vocals/instrumental); production (lo-fi, tape saturation, wide stereo, dry, vintage); structure (intro, build, drop, outro).
- **Suno specifics [Secondary]:** section tags `[Intro] [Verse] [Chorus] [Bridge] [Outro]` in lyrics; adding a short cue per tag (`[Verse 1 - whispered]`) and keeping three or fewer bracketed descriptors per section (https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/creative/creative-songwriting-and-ai-music); V5 and V5.5 (March 2026) style box 1,000 characters, lyrics box 5,000 characters (same source); API wrapper has negative tags for exclusions (https://www.mintlify.com/gcui-art/suno-api/guides/custom-mode). No official Suno help page was retrieved: **all Suno details [Secondary]**.
- **Udio:** not researched this session **[Unverified]**.
- **Caveat:** Naming real artists is restricted on major music generators; describe the sound instead. Check each tool's license terms for commercial game use.

### 5.12 SFX layering
- **Definition:** Building one sound from several stacked parts, each covering a role: a sharp transient (attack), a body (weight, low end), a texture or sweetener (debris, sparkle), and a tail. E.g. a sword hit = metal clang + low thump + whoosh tail.
- **Example:** Generate `metal sword impact, sharp`, `low punchy thud`, `short metallic ring-out` separately and layer them.
- **Source:** **[Craft]**.

### 5.13 Transient, attack, tail (and the envelope)
- **Definition:** The **transient** is the short, high-energy start of a sound; **attack** is how quickly it reaches peak; **decay/sustain/release** (ADSR) describe how it falls and holds; the **tail** is the fading end (natural ring or reverb). UI sounds want fast attacks and short tails; ambiences want slow attacks and long tails. **[Craft]**
- **Example (ElevenLabs SFX):** `short UI confirm chime, fast attack, bright, very short tail, 0.5 seconds`
- **Source:** ElevenLabs Sound Effects: duration 0.5 to 30 s, auto when unset; `prompt_influence` default 0.3 on 0 to 1 (higher = closer to prompt, less variation). https://www.mintlify.com/elevenlabs/elevenlabs-python/api-reference/audio/sound-effects **[Secondary]** (SDK docs mirror). The 30 s maximum conflicts with a 22 s figure on fal.ai **[Unverified]**.

### 5.14 Foley
- **Definition:** Everyday sounds performed and recorded in sync with picture (footsteps, cloth rustle, props, doors), named after Jack Foley. In AI prompting, "foley" signals realistic, close, human-scale sounds. **[Craft]**
- **Example:** `foley: leather boots on wet gravel, slow walk, close-mic'd, dry`
- **Caveat:** Ask for one action per generation; "footsteps and door and rain" mixes them into one file you cannot rebalance.

### 5.15 Adaptive (interactive) game audio
- **Horizontal re-sequencing:** Music is split into segments (explore, combat, victory) and the game switches between them at musical boundaries (next beat, bar, or marked exit point), often through transition segments.
- **Vertical layering (vertical remixing):** One piece is split into stacked stems that play in sync; the game fades layers in or out with intensity (add drums when enemies appear).
- **Sources:** Definitions and middleware transition rules: https://sounddesign.irpr.agency/glossary/horizontal-resequencing/ and https://sounddesign.irpr.agency/glossary/adaptive-music/ **[Secondary]**. Official Wwise/FMOD manual pages not retrieved **[Unverified]**.
- **Example:** `Same track as three stems at identical length and BPM: (1) ambient pad only, (2) add percussion, (3) add full brass. 16 bars, loopable.`
- **Caveat:** Generators do not reliably output aligned stems of one composition. Generate the full mix once and separate, or compose layers from one exported stem set.

### 5.16 Ducking
- **Definition:** Automatically lowering music or ambience when dialogue or an important SFX plays, typically by sidechain compression or a mixer snapshot. **[Craft]**

### 5.17 Headroom and clipping
- **Definition:** Headroom is the space between the loudest peak and 0 dBFS. Clipping is distortion when signal exceeds 0 dBFS. Keep peaks below about -1 dBTP on delivered files (Spotify recommendation above **[Official]**).

### 5.18 Mono vs stereo, spatial audio
- **Definition:** Positional game SFX are usually delivered **mono** so the engine can place them in 3D; music and ambiences are usually stereo. **[Craft]**
- **Caveat:** A stereo footstep cannot be positioned correctly by most engines' 3D panners without downmixing.

---

## 6. Voice

### 6.1 Voice direction vocabulary
- **Pace (tempo):** Speed of speech; `slow, deliberate` vs `rapid-fire`. **[Craft]**
- **Pitch and intonation:** How high/low and how the pitch moves; `rising, questioning intonation`, `flat monotone`. **[Craft]**
- **Timbre:** Tone color of a voice; `gravelly, breathy, nasal, warm, raspy, bright`. **[Craft]**
- **Delivery / read:** Overall performance style; `conversational read`, `announcer read`, `deadpan`, `projected to the back of a hall`. **[Craft]**
- **Emotion and intention:** What the character feels and wants; directors give intention ("you are trying to calm her down") rather than just emotion labels. **[Craft]**
- **Emphasis (stress):** Which word carries weight; changes meaning ("*I* didn't take it" vs "I didn't *take* it"). Use italics or caps sparingly depending on tool. **[Craft]**
- **Example:** `Old ship captain, gravelly low voice, slow pace, tired but warm, as if telling a story he has told a hundred times.`

### 6.2 SSML basics
- **Definition:** Speech Synthesis Markup Language, a W3C XML standard for controlling TTS: `<speak>`, `<break time="500ms"/>` (pause), `<emphasis>`, `<prosody rate="slow" pitch="+2st">`, `<say-as interpret-as="date">`, `<phoneme alphabet="ipa" ph="...">`, `<sub alias="...">` (say something else). **[Craft]** (W3C SSML 1.1; not fetched this session).
- **Caveat:** Each TTS vendor supports a different subset; check before relying on any tag.

### 6.3 ElevenLabs pauses and pronunciation
- **Break tag:** `<break time="1.5s" />` for pauses up to 3 seconds; too many in one generation can destabilize output; dashes or ellipses are less consistent alternatives. https://elevenlabs.io/docs/best-practices/prompting/controls **[Official]**. Whether Eleven v3 supports break tags: **[Unverified]**.
- **Phoneme tags:** SSML `<phoneme>` with IPA or CMU Arpabet; docs say CMU Arpabet "generally offers more reliable performance"; tags apply to single words; include stress numbers, e.g. `T AE1 L AH0 N` for "talon". https://elevenlabs.io/docs/best-practices/prompting/pronunciation **[Official]**. Supported models conflict across doc versions (Flash v2 only vs Flash v2, Turbo v2 and English v1) **[Unverified]**.
- **Example:** `<phoneme alphabet="cmu-arpabet" ph="K AY1 R AH0 N">Kyron</phoneme>`
- **Other pronunciation fixes:** phonetic respelling in plain text ("Kai-ron"); pronunciation dictionaries and alias rules (ElevenLabs offers them; details not retrieved **[Unverified]**); normalization (write numbers, dates and symbols as words: "twenty twenty-six") https://elevenlabs.io/docs/best-practices/prompting/normalization **[Official]** (page exists; contents not extracted).

### 6.4 ElevenLabs Eleven v3 audio tags
- **Definition:** Bracketed cues inline in the text that steer delivery or add non-speech sounds, e.g. `[whispers]`, `[laughs]`, `[sighs]`, `[sarcastic]`, `[excited]`.
- **Example:** `[whispers] Did you hear that? [pause] [nervously] I think it came from the attic.`
- **Sources:** Official v3 guide: very short prompts give inconsistent output, so use prompts over 250 characters; the voice you choose is the most important parameter and must suit the delivery (a shouting voice tagged `[whispering]` likely won't work). https://elevenlabs.io/docs/best-practices/prompting **[Official]**. Tags only bend delivery within the voice's range; a few tags work, five in one bracket confuse; generate 2 or 3 takes: https://runware.ai/docs/models/elevenlabs-v3/guides/directing-with-audio-tags **[Secondary]**. Exact `[pause]` support **[Unverified]**.
- **Caveats:** The model was labeled "alpha" in the guide title when seen. v3 accepts IPA between slashes directly in text (reported in search extract of the official best-practices pages) **[Unverified]**.

### 6.5 ElevenLabs v3 stability modes
- **Definition:** In v3, stability is "the most important setting", controlling how closely output adheres to the reference voice. Modes: **Creative** (more emotional and expressive, prone to hallucination), **Natural** (balanced), **Robust** (most stable, less responsive to tags).
- **Source:** https://elevenlabs.io/docs/best-practices/prompting **[Official]** for the setting and the Creative description. Natural and Robust descriptions **[Secondary]** (lower stability makes tags more responsive; higher flattens them: runware.ai guide above).

### 6.6 ElevenLabs voice settings (API)
- **Stability:** default 0.5; lower = broader emotional range; higher = can become monotonous.
- **Similarity boost:** default 0.75; higher = closer to the original voice.
- **Style (exaggeration):** default 0; ElevenLabs generally recommends keeping it at 0 because it makes the model slightly less stable.
- **Speaker boost:** default true; improves similarity and clarity at some latency cost; not available for Eleven v3.
- **Speed:** default 1.0.
- **Source:** https://elevenlabs.io/docs/api-reference/voices/settings.md **[Official]**. Speed range: SDK docs say 0.25 to 4.0, recommended 0.5 to 2.0 (https://www.mintlify.com/elevenlabs/elevenlabs-python/api-reference/voices/settings **[Secondary]**); the product UI range may be narrower (commonly cited 0.7 to 1.2) **[Unverified]**.
- **Example:** `stability 0.35, similarity_boost 0.8, style 0` for an expressive game character.

### 6.7 Voice cloning and voice design
- **Definition:** Cloning builds a voice from recordings of a real speaker; voice design creates a new synthetic voice from a text description.
- **Example (design prompt):** `young adult female, light Irish accent, bright and quick, slightly raspy, cheerful shopkeeper`
- **Source:** **[Craft]** for the concepts.
- **Caveat:** Only clone voices you have explicit permission to use; most platforms require consent verification.

### 6.8 Takes and selects
- **Definition:** Generate several takes of each line and pick the best (a "select"), as in a real recording session.
- **Source:** "running two or three generations and picking the best take" (runware.ai v3 guide) **[Secondary]**.

### 6.9 Line formatting for games (barks, dialogue)
- **Definition:** Barks are short reactive lines (`"Reloading!"`, `"Over there!"`); keep each as its own file with a consistent naming scheme and leave short silence handles at the start and end. **[Craft]**
- **Caveat:** Very short lines are exactly where v3 is least consistent (short-prompt warning above **[Official]**); pad with context and trim the audio.

---

## 7. Ten common mistakes in media prompts, with fixes

1. **Keyword soup instead of a scene.** `castle, epic, 8k, trending, masterpiece` gives generic results. **Fix:** Write one or two clear sentences filling the slots in 1.1. Imagen's guide asks for descriptive and clear prompts (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide **[Official]**).
2. **Saying what you do not want in the main prompt.** "No people, no text" can add people and text, and Runway Gen-4 says negative phrasing can produce the opposite (https://help.runwayml.com/hc/en-us/articles/39789879462419 **[Official]**). **Fix:** Describe the positive ("empty street", "locked camera"), or use the tool's real negative field if it has one (1.3).
3. **Re-describing the input image in image-to-video.** **Fix:** Describe only motion, camera and timing (https://help.runwayml.com/hc/en-us/articles/48324313115155 **[Official]**).
4. **Too many actions per clip.** Five events in 8 seconds produce mush. **Fix:** One subject, one action, one camera move per clip; cut clips together in an editor.
5. **Confusing zoom with dolly (and pan with truck).** **Fix:** Use the exact term from 3.4 and add "the camera physically moves" or "no zoom" when it matters.
6. **Asking for "transparent background" from a model that cannot output alpha.** You get a painted checkerboard. **Fix:** Use a model with a transparency setting (OpenAI `background: transparent` with PNG/WebP **[Official]**) or remove the background afterward.
7. **"Pixel art" at 1024px with no grid or palette.** **Fix:** State native resolution and palette size, then downscale with nearest-neighbor and quantize (4.4).
8. **Changing many things between iterations.** **Fix:** Lock the seed (where available) or the reference image, and change one variable at a time; keep a reusable style block for set consistency (1.4, 1.14).
9. **Generating game audio as finished, baked, mixed files.** Music with intros and fades will not loop; SFX with reverb cannot be re-spaced; stereo SFX cannot be positioned. **Fix:** Ask for loopable bars with no intro/outro at a stated BPM, dry mono SFX, one action per file, and master to the platform target (-14 LUFS Spotify **[Official]**; about -18 LUFS mobile game, -24 LUFS console **[Secondary]**).
10. **Fighting the voice instead of choosing the right one.** Stacking `[excited] [shouting]` on a calm narrator voice, or using very short lines. **Fix:** Pick a voice whose natural range fits the role, keep tags few, give longer context (ElevenLabs recommends prompts over 250 characters for v3 **[Official]**), and generate several takes.

---

## Item counts

| Section | Items |
|---|---|
| 1. Image prompting | 14 |
| 2. Photo and cinematography (subsections; 9 shot sizes, 8 angles, 11 lighting terms, 9 grading terms inside) | 6 |
| 3. Video generation (plus 16 camera moves in the table) | 11 |
| 4. Game art | 11 |
| 5. Audio | 18 |
| 6. Voice | 9 |
| 7. Common mistakes | 10 |

## Not verified (check before print)

- Every URL was verified only through search-engine extracts; WebFetch and direct network access were blocked by policy in this session.
- Midjourney: V8.2 default date (secondary only); whether `--oref`/`--ow` work on V8.x; seed range on the official page; `--ow` default.
- OpenAI: whether any GPT Image model accepts a negative prompt (believed not); "up to 16 reference images" for gpt-image-2; how strictly masks are honored.
- Google: which Imagen versions still honor `negativePrompt`; Veo allowed durations (4/6/8 s) and output frame rate; Veo negative prompt field; scene-extension length and chain limit.
- FLUX.2 "no negative prompts" and JSON-prompt claims are from partner/third-party docs, not docs.bfl.ai.
- Stability AI parameters are from ComfyUI's docs for the Stability API node, not Stability's own API reference.
- Kling 3.0 durations (3 to 15 s), multi-shot limits, native negative prompt, and Motion Control settings are from third-party guides; only the camera-control page is official.
- Higgsfield: dolly zoom and Cinema Studio settings are secondary; no official parameter documentation found.
- ElevenLabs: Natural/Robust stability definitions; speed range in the UI; break-tag support on v3; phoneme-tag model support (doc versions conflict); IPA-between-slashes on v3; pronunciation dictionary and alias details; sound effects max duration (30 s vs 22 s) and loop default.
- Suno: all details are from third-party guides (no official help page retrieved), including V5.5 date and box limits. Udio was not researched.
- Apple Music Sound Check behavior; YouTube peak guidance; current Sony ASWG console figure (-24 vs older -23 LUFS); 48 kHz as a formal game standard.
- Official Wwise/FMOD wording for adaptive music; Unity Sprite Atlas official page; Lospec palette list.
- Craft-labeled definitions (shot sizes, camera moves, lighting, EQ, compression, SSML tags) are standard vocabulary but were not tied to a fetched source this session.
