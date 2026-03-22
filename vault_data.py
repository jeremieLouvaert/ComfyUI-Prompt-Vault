"""
Prompt Vault — Component Database & Curated Template Library

The photographic knowledge base. Real camera gear, real lighting setups,
real film stocks. No AI slop, no generic modifiers.
"""

# ---------------------------------------------------------------------------
# CAMERA + LENS COMBOS
# Organized by use case. Each entry: (display_name, prompt_fragment)
# ---------------------------------------------------------------------------

CAMERAS = {
    # --- Portrait / Fashion ---
    "Sony A7R V + 85mm f/1.4 GM": "Shot on Sony A7R V with 85mm f/1.4 G Master lens, shallow depth of field, natural skin rendering",
    "Canon R5 + RF 85mm f/1.2L": "Captured with Canon EOS R5 and RF 85mm f/1.2L USM lens, creamy bokeh, precise autofocus on eyes",
    "Nikon Z9 + 105mm f/1.4": "Photographed with Nikon Z9 and Nikkor Z 105mm f/1.4 S, medium telephoto compression, buttery bokeh",
    "Hasselblad X2D + 80mm f/1.9": "Shot on Hasselblad X2D 100C with XCD 80mm f/1.9 lens, medium format rendering, exceptional tonal depth",
    "Leica SL2 + 50mm f/1.4 Summilux": "Captured with Leica SL2 and 50mm f/1.4 Summilux-SL ASPH, Leica color science, natural rendering",
    "Phase One IQ4 + 110mm f/2.8": "Shot on Phase One IQ4 150MP with Schneider Kreuznach 110mm f/2.8, medium format, extraordinary detail",
    "Fujifilm GFX 100S + 80mm f/1.7": "Photographed with Fujifilm GFX 100S and GF 80mm f/1.7 R WR, medium format depth, Fuji color science",

    # --- Editorial / Street ---
    "Sony A7 IV + 35mm f/1.4 GM": "Shot on Sony A7 IV with 35mm f/1.4 G Master lens, environmental framing, street photography perspective",
    "Leica M11 + 35mm f/1.4 Summilux": "Captured with Leica M11 and 35mm f/1.4 Summilux-M ASPH, rangefinder rendering, classic Leica tonality",
    "Canon R5 + RF 28-70mm f/2L": "Photographed with Canon EOS R5 and RF 28-70mm f/2L USM, versatile focal range, constant f/2 aperture",
    "Nikon Z8 + 50mm f/1.2 S": "Shot on Nikon Z8 with Nikkor Z 50mm f/1.2 S, standard perspective, exceptional low-light rendering",
    "Ricoh GR IIIx": "Captured with Ricoh GR IIIx, 40mm equivalent, compact street photography aesthetic, subtle grain",

    # --- Landscape / Architecture ---
    "Sony A7R V + 24mm f/1.4 GM": "Shot on Sony A7R V with 24mm f/1.4 G Master, wide-angle environmental perspective, deep depth of field",
    "Canon R5 + RF 14-35mm f/4L": "Captured with Canon EOS R5 and RF 14-35mm f/4L IS USM, ultra-wide architectural perspective",
    "Nikon Z9 + 14-24mm f/2.8 S": "Photographed with Nikon Z9 and Nikkor Z 14-24mm f/2.8 S, ultra-wide landscape perspective",
    "Fujifilm GFX 100S + 23mm f/4": "Shot on Fujifilm GFX 100S with GF 23mm f/4 R LM WR, medium format wide angle, expansive field of view",

    # --- Product / Macro ---
    "Canon R5 + RF 100mm f/2.8L Macro": "Captured with Canon EOS R5 and RF 100mm f/2.8L Macro IS USM, 1:1 magnification, extreme detail",
    "Sony A7R V + 90mm f/2.8 Macro": "Shot on Sony A7R V with FE 90mm f/2.8 Macro G OSS, precise macro detail, natural color rendering",
    "Hasselblad X2D + 120mm f/3.5 Macro": "Photographed with Hasselblad X2D and XCD 120mm f/3.5 Macro, medium format macro, exceptional sharpness",

    # --- Telephoto / Sports ---
    "Sony A1 + 70-200mm f/2.8 GM II": "Shot on Sony A1 with 70-200mm f/2.8 GM II, compressed perspective, subject isolation at distance",
    "Canon R3 + RF 70-200mm f/2.8L": "Captured with Canon EOS R3 and RF 70-200mm f/2.8L IS USM, fast telephoto compression, action-ready",
    "Nikon Z9 + 70-200mm f/2.8 VR S": "Photographed with Nikon Z9 and Nikkor Z 70-200mm f/2.8 VR S, telephoto isolation, precise tracking",

    # --- Classic / Vintage ---
    "Mamiya RZ67 + 110mm f/2.8": "Shot on Mamiya RZ67 with Sekor Z 110mm f/2.8, medium format film camera, classic portrait rendering",
    "Contax 645 + 80mm f/2": "Captured with Contax 645 and Zeiss Planar 80mm f/2, legendary medium format rendering, film-era tonality",
    "Pentax 67 + 105mm f/2.4": "Photographed with Pentax 67 and SMC 105mm f/2.4, the 'portrait king' medium format, massive bokeh",

    # --- Cinematic ---
    "RED V-Raptor + Cooke S7/i 75mm": "Captured with RED V-Raptor 8K and Cooke S7/i 75mm T2.0, cinematic motion picture rendering, anamorphic bokeh",
    "ARRI Alexa 35 + Zeiss Supreme 50mm": "Shot on ARRI Alexa 35 with Zeiss Supreme Prime 50mm T1.5, Hollywood-grade cinematic rendering",
}

# ---------------------------------------------------------------------------
# LIGHTING SETUPS
# Real photography lighting terminology, not generic "cinematic lighting"
# ---------------------------------------------------------------------------

LIGHTING = {
    # --- Studio ---
    "Rembrandt (classic portrait)": "Rembrandt lighting with triangular cheek highlight, key light 45 degrees camera-left at 45 degrees elevation, 3:1 lighting ratio",
    "Butterfly / Paramount": "Butterfly lighting with key light directly above and in front of subject, creating shadow under nose, glamour portrait style",
    "Split light (dramatic)": "Split lighting with key light at 90 degrees to subject, illuminating exactly half the face, dramatic mood",
    "Clamshell (beauty)": "Clamshell lighting with key light above and fill below at equal distance, minimal shadows, beauty/cosmetic photography",
    "Loop lighting (natural portrait)": "Loop lighting with key light 30-45 degrees to one side, small shadow from nose falling toward cheek, universally flattering",
    "Broad light (editorial)": "Broad lighting illuminating the side of face turned toward camera, widening appearance, editorial fashion aesthetic",
    "Beauty dish + fill": "Beauty dish as key light creating focused specular highlight with soft falloff, white fill card below chin, beauty/fashion editorial",
    "Three-point (professional)": "Classic three-point lighting: key light camera-left creating defining shadows, fill light camera-right at half power, rim light behind subject separating from background",
    "High-key studio": "High-key studio lighting with multiple softboxes creating even, shadow-free illumination, white background, clean commercial aesthetic",
    "Low-key dramatic": "Low-key studio lighting with single focused light source, deep shadows, dark background, moody dramatic portrait",
    "Ring light (fashion)": "Ring light centered on lens axis, even facial illumination, distinctive circular catchlights in eyes, fashion/beauty aesthetic",
    "Strip lights (edge definition)": "Twin strip softboxes positioned at 90 degrees to subject on each side, creating rim highlights defining body contour, editorial fashion",

    # --- Natural ---
    "Golden hour (warm)": "Golden hour natural light, warm directional sunlight at low angle, long shadows, skin-warming tones, sun flare optional",
    "Blue hour (cool moody)": "Blue hour ambient light, cool desaturated tones, soft even illumination, contemplative mood, no harsh shadows",
    "Overcast diffused": "Overcast sky acting as giant softbox, soft even diffused lighting, no harsh shadows, natural skin tones, true color rendering",
    "Window light (soft directional)": "Single large window providing soft directional natural light, gradual shadow falloff across face, painterly quality",
    "Dappled shade": "Dappled light filtering through trees or lattice, creating organic light-shadow patterns on subject, natural environmental mood",
    "Harsh midday sun": "Direct overhead midday sunlight, strong defined shadows, high contrast, raw documentary aesthetic",
    "Backlit / rim silhouette": "Strong backlight behind subject creating rim highlight and partial silhouette, face in shadow with subtle fill, dramatic separation",
    "Open shade (even)": "Open shade providing soft, even illumination from reflected sky light, no direct sun, consistent neutral tones",

    # --- Mixed / Practical ---
    "Neon practical lights": "Practical neon lighting from environment, mixed color temperature, urban night aesthetic, colored light spill on skin",
    "Tungsten warm interior": "Warm tungsten interior lighting, 3200K color temperature, intimate domestic atmosphere, orange-warm skin tones",
    "Fluorescent (institutional)": "Overhead fluorescent lighting, slightly green color cast, institutional/documentary aesthetic, unflattering but authentic",
    "Candlelight intimate": "Candlelight illumination, extremely warm color temperature, soft flickering quality, intimate low-light atmosphere, visible flame catchlights",
}

# ---------------------------------------------------------------------------
# FILM STOCKS / COLOR SCIENCE
# Real film emulsions and their characteristics
# ---------------------------------------------------------------------------

FILM_STOCKS = {
    # --- Color Negative ---
    "Kodak Portra 400": "Kodak Portra 400 color rendering: muted warm tones, exceptional skin reproduction, fine grain, slight pastel quality, wedding/portrait standard",
    "Kodak Portra 160": "Kodak Portra 160 rendering: finer grain than 400, subtle color palette, lower contrast, pristine skin tones, studio portrait ideal",
    "Kodak Portra 800": "Kodak Portra 800 rendering: visible but pleasing grain, warm tones pushed further, low-light versatility, editorial night aesthetic",
    "Kodak Ektar 100": "Kodak Ektar 100 rendering: vivid saturated colors, ultra-fine grain, high contrast, punchy landscapes, the sharpest color negative film",
    "Kodak Gold 200": "Kodak Gold 200 rendering: consumer-warm tones, noticeable grain, nostalgic amateur aesthetic, slightly yellow-green cast",
    "Fuji Pro 400H": "Fujifilm Pro 400H rendering: cool-neutral tones, pastel highlights, green-shifted shadows, fine grain, fashion/editorial favorite",
    "Fuji Superia 400": "Fujifilm Superia 400 rendering: consumer-grade visible grain, green-tinged shadows, warm highlights, everyday nostalgia",
    "Cinestill 800T": "CineStill 800T rendering: tungsten-balanced, halation glow around highlights, cinematic color shifts, red-orange halos on bright lights, night photography standard",
    "Cinestill 50D": "CineStill 50D rendering: daylight-balanced cinema stock, incredibly fine grain, rich color depth, high dynamic range, clean studio aesthetic",

    # --- Black & White ---
    "Kodak Tri-X 400": "Kodak Tri-X 400 rendering: classic photojournalism grain, rich midtones, deep blacks, slightly gritty, the standard for documentary B&W",
    "Ilford HP5 Plus 400": "Ilford HP5 Plus 400 rendering: versatile B&W, slightly softer grain than Tri-X, excellent shadow detail, push-processable, European tonal quality",
    "Ilford Delta 3200": "Ilford Delta 3200 rendering: heavy atmospheric grain, extreme low-light capability, dramatic tonal separation, concert/night B&W",
    "Kodak T-Max 100": "Kodak T-Max 100 rendering: extremely fine grain B&W, smooth tonal gradation, precise detail, technical/studio B&W standard",

    # --- Slide / Transparency ---
    "Fuji Velvia 50": "Fujichrome Velvia 50 rendering: hyper-saturated colors, deep contrast, vivid greens and reds, landscape transparency standard, punchy and dramatic",
    "Kodak Ektachrome E100": "Kodak Ektachrome E100 rendering: accurate natural colors, fine grain transparency, neutral-cool tones, faithful color reproduction",

    # --- Digital Color Science ---
    "Clean digital (no film emulation)": "Clean modern digital rendering, neutral color science, no film grain, maximum sharpness and dynamic range",
    "Fujifilm Classic Chrome": "Fujifilm Classic Chrome color profile: desaturated warm tones, slightly muted, documentary/street aesthetic, digital film simulation",
    "Fujifilm Classic Neg": "Fujifilm Classic Neg color profile: high contrast, amber highlights, cyan-shifted shadows, punchy modern-retro, the TikTok film look",
}

# ---------------------------------------------------------------------------
# MOOD / ATMOSPHERE
# ---------------------------------------------------------------------------

MOODS = {
    "Intimate & quiet": "Intimate, contemplative atmosphere, quiet emotional tension, personal space, soft focus on human connection",
    "Editorial confidence": "Editorial confidence and power, strong deliberate posing, direct gaze, fashion authority, commanding presence",
    "Melancholic nostalgia": "Melancholic nostalgic mood, wistful distant gaze, faded warmth, sense of memory and longing, bittersweet beauty",
    "Raw documentary": "Raw documentary realism, unposed authenticity, imperfect framing, decisive moment, photojournalistic truth",
    "Luxurious opulence": "Luxurious opulent atmosphere, rich textures, premium materials visible, wealth coded through craft and detail, aspirational elegance",
    "Gritty urban": "Gritty urban energy, street texture, environmental context, lived-in authenticity, city pulse visible in every surface",
    "Serene minimalism": "Serene minimalist mood, negative space, clean composition, breathing room, quiet visual clarity",
    "Cinematic tension": "Cinematic tension and suspense, dramatic light-shadow play, narrative implication, the moment before something happens",
    "Warm golden comfort": "Warm golden comfort, sunlit ease, relaxed joy, natural warmth, the feeling of a perfect afternoon",
    "Cool ethereal dream": "Cool ethereal dreamlike quality, soft diffusion, muted palette, otherworldly calm, floating between real and imagined",
    "Fierce & bold": "Fierce bold energy, high contrast, saturated impact, unapologetic power, visual punch that demands attention",
    "Candid natural": "Candid natural moment, un-directed authenticity, mid-action, genuine expression, the beauty of not performing for camera",
    "Dark & moody": "Dark moody atmosphere, heavy shadows, restrained palette, brooding intensity, emotional weight in every tone",
    "Playful & energetic": "Playful energetic mood, movement and motion, genuine laughter, dynamic posing, spontaneous joy captured mid-frame",
    "Stoic & timeless": "Stoic timeless dignity, classical posing reference, enduring beauty, portrait that could exist in any era",
}

# ---------------------------------------------------------------------------
# QUALITY DIRECTIVES (Anti-AI-look packages)
# ---------------------------------------------------------------------------

QUALITY_DIRECTIVES = {
    "Ultra-realism (anti-AI)": "Hyper-realistic with natural imperfections: visible skin pores, subtle blemishes, asymmetric features, micro-wrinkles around eyes, individual hair strands with flyaways, fabric texture at thread level. No airbrushing, no plastic skin, no uncanny symmetry. Looks indistinguishable from a photograph.",
    "Editorial print-ready": "Editorial print-quality: tack-sharp focus on eyes, natural skin texture preserved, fabric weave visible, subtle catchlights in irises, controlled depth of field, color-accurate for CMYK reproduction. Magazine-ready without retouching.",
    "Fine art photography": "Fine art photographic quality: intentional grain structure, considered tonal range, printable at large format, gallery-exhibition standard, archival quality rendering.",
    "Commercial product": "Commercial product photography standard: razor-sharp detail, accurate material rendering (metal reflections, glass refractions, fabric drape), clean studio execution, e-commerce ready, color-accurate.",
    "Documentary authenticity": "Documentary photographic authenticity: un-retouched, environmental context visible, available-light rendering, imperfect framing acceptable, truth over beauty, visible wear and aging on surfaces.",
    "Cinematic frame": "Cinematic still frame quality: 2.39:1 anamorphic framing reference, motivated lighting, narrative composition, color graded for mood, could be a freeze-frame from a film.",
    "RAW unprocessed": "RAW file aesthetic: flat contrast curve, full dynamic range preserved, neutral color temperature, no creative grading applied, photographer's starting point.",
}

# ---------------------------------------------------------------------------
# COMPOSITION / FRAMING
# ---------------------------------------------------------------------------

COMPOSITIONS = {
    "Rule of thirds": "Composed using rule of thirds, subject placed on power point intersection, balanced negative space",
    "Center weighted": "Center-weighted composition, subject commanding center frame, symmetrical balance, formal portrait framing",
    "Golden ratio": "Golden ratio spiral composition, organic visual flow leading eye through frame, mathematically pleasing proportion",
    "Environmental portrait": "Environmental portrait framing, subject in context of their surroundings, wider framing showing location and atmosphere",
    "Tight crop (beauty)": "Tight beauty crop, face filling frame from forehead to chin, extreme detail emphasis, intimate perspective",
    "Full body editorial": "Full body editorial framing, head-to-toe with breathing room, posture and silhouette as compositional element",
    "Dutch angle (dynamic)": "Dutch angle tilt creating dynamic tension, diagonal leading lines, sense of energy or unease",
    "Over-the-shoulder": "Over-the-shoulder composition, depth layering with foreground element, voyeuristic perspective, narrative framing",
    "Negative space (minimal)": "Expansive negative space composition, subject occupying small portion of frame, isolation and emphasis through emptiness",
    "Leading lines": "Leading lines composition, environmental geometry directing eye to subject, architectural or natural lines converging on focal point",
}

# ---------------------------------------------------------------------------
# SUBJECT CATEGORIES (for Browse mode filtering)
# ---------------------------------------------------------------------------

CATEGORIES = [
    "portrait",
    "fashion-editorial",
    "product",
    "architecture",
    "landscape",
    "street-documentary",
    "food-drink",
    "beauty-closeup",
]

# ---------------------------------------------------------------------------
# CURATED TEMPLATE LIBRARY
# The survivors. Each one earned its place.
# ---------------------------------------------------------------------------

TEMPLATES = [
    # --- PORTRAIT ---
    {
        "id": "portrait_headshot_studio",
        "name": "Professional Studio Headshot",
        "category": "portrait",
        "prompt": "A professional high-resolution profile portrait. Chest-up composition, centered with natural posture and direct eye contact. Styled for a premium photo studio session, wearing a tailored smart-casual charcoal gray blazer with refined fabric grain and subtle thread texture. Background: solid neutral dark gray studio backdrop with subtle gradient, lighter behind subject, darker toward edges. Shot on Sony A7R V with 85mm f/1.4 G Master lens. Classic three-point lighting: soft key light creating defining facial shadows, subtle rim light separating shoulders from background. Natural skin texture with visible pores, not airbrushed. Natural catchlights in eyes. Fabric shows subtle wool texture. Ultra-realistic 8K professional headshot.",
        "tags": ["headshot", "studio", "professional", "corporate"],
        "source": "awesome-nanobanana-pro",
    },
    {
        "id": "portrait_film_emotional",
        "name": "Kodak Portra Emotional Portrait",
        "category": "portrait",
        "prompt": "A cinematic emotional portrait shot on Kodak Portra 400 film. Setting: urban street coffee shop window at golden hour, warm nostalgic lighting hitting the side of the face. Subtle film grain and soft focus creating a dreamy storytelling vibe. Subject looking slightly away from camera, holding a coffee cup, relaxed candid expression. Depth of field with bokeh background of city lights. High quality, authentic film texture, genuine human moment.",
        "tags": ["film", "emotional", "golden-hour", "candid", "portra"],
        "source": "awesome-nanobanana-pro",
    },
    {
        "id": "portrait_1990s_flash",
        "name": "1990s Camera Flash Portrait",
        "category": "portrait",
        "prompt": "A portrait captured with a 1990s-style camera using direct front flash. Messy dark brown hair tied up, calm yet playful smile. Modern oversized cream sweater. Background: dark white wall covered with aesthetic magazine posters and stickers, evoking a cozy bedroom atmosphere under dim lighting. 35mm lens flash creating a nostalgic glow. Subtle grain, retro highlights, crisp details, soft shadows. Authentic analog camera aesthetic.",
        "tags": ["retro", "90s", "flash", "nostalgic", "film"],
        "source": "awesome-nanobanana-pro",
    },
    {
        "id": "portrait_dramatic_spotlight",
        "name": "Dramatic Spotlight Portrait",
        "category": "portrait",
        "prompt": "A dramatically lit portrait against a completely black background. Narrow beam spotlight focused only on the center of the face, sharp edges to the light. All areas outside the spotlight fall quickly into deep darkness with high shadow falloff, blending into the black background. Long dark hair with strands falling over the face, lower parts fading into shadows. One hand raised gently near lips. Eyes looking directly at camera with mysterious mood. Dark, moody, dramatic, mysterious tone. High contrast only in the lit portion of the face. Everything outside the spotlight nearly invisible.",
        "tags": ["dramatic", "spotlight", "dark", "moody", "chiaroscuro"],
        "source": "awesome-nanobanana-pro",
    },
    {
        "id": "portrait_hasselblad_studio",
        "name": "Hasselblad Medium Format Studio Portrait",
        "category": "portrait",
        "prompt": "Ultra-high resolution portrait captured with Hasselblad H6D-400C at f/2.8. Professional model with detailed iris structure captured in natural light mixed with soft studio fill. Wearing tailored designer blazer over minimalist white top. Background is clean gradient with subtle texture. Micro-detail rendering of individual eyelashes, skin pore texture, and fabric threading. Shot in controlled studio environment with butterfly lighting configuration and silver reflector fill. Shallow depth of field isolating subject from background with smooth medium format bokeh.",
        "tags": ["medium-format", "hasselblad", "studio", "detail", "fashion"],
        "source": "claude-prompts",
    },
    {
        "id": "portrait_stoic_timeless",
        "name": "Timeless Black & White Portrait",
        "category": "portrait",
        "prompt": "A timeless black and white portrait in the tradition of Irving Penn and Richard Avedon. Simple light gray studio background. Subject in dark clothing, direct unflinching gaze. Shot on medium format with 110mm lens at f/4. Single large softbox camera-left providing dimensional light, deep shadows on opposite side. Kodak Tri-X 400 grain structure, rich midtones, pure blacks without crushing detail. Printed on silver gelatin. Skin texture, laugh lines, and character marks all preserved — beauty through authenticity, not despite it.",
        "tags": ["black-white", "timeless", "fine-art", "studio", "classic"],
        "source": "original",
    },

    # --- FASHION / EDITORIAL ---
    {
        "id": "fashion_vogue_studio",
        "name": "Vogue Studio Editorial",
        "category": "fashion-editorial",
        "prompt": "A Vogue magazine editorial photoshoot in a studio with cream and gold gradient backdrop. Subject wearing an intricate haute couture gown with silver accents and a dramatic train. Soft diffused lighting with subtle backlighting creating a luminous halo effect. Shot using Leica Summilux-M 35mm f/1.4 ASPH at f/1.4 aperture. Shallow depth of field highlighting facial details and dress texture. Composition captures elegance and high fashion with precise posing and editorial confidence. Ultra-realistic rendering with visible fabric weave and skin detail.",
        "tags": ["vogue", "haute-couture", "studio", "editorial", "luxury"],
        "source": "claude-prompts",
    },
    {
        "id": "fashion_golden_hour_location",
        "name": "Golden Hour Location Fashion",
        "category": "fashion-editorial",
        "prompt": "Fashion editorial shot on location during golden hour. Subject in structured designer blazer, wind catching fabric showing drape and movement. Mediterranean coastal setting with warm stone architecture behind. Shot on Hasselblad X2D with 80mm f/1.9 lens, shallow depth of field separating subject from environment. Golden directional sunlight from camera-left creating warm rim highlight on hair and shoulder. Natural skin texture, visible fabric grain, environmental context. Editorial confidence in posing, direct gaze. Warm but not oversaturated color palette.",
        "tags": ["golden-hour", "location", "editorial", "mediterranean", "fashion"],
        "source": "original",
    },
    {
        "id": "fashion_beauty_macro",
        "name": "Beauty Macro Close-Up",
        "category": "beauty-closeup",
        "prompt": "Ultra-detailed macro beauty close-up. Extreme detail on skin texture — visible pores, fine peach fuzz, natural sebum shine on cheekbones. Glossy lip texture with individual lip lines visible. Individual eyelash strands with subtle mascara clumping. Studio beauty dish lighting from above creating butterfly shadow under nose, white fill card below chin for open shadows. Shot on Canon R5 with RF 100mm f/2.8L Macro at f/4, tack-sharp focus plane on eyes and lips. Clean studio backdrop. No retouching, no airbrushing — the beauty is in the real texture.",
        "tags": ["beauty", "macro", "closeup", "skin-detail", "studio"],
        "source": "original",
    },
    {
        "id": "fashion_film_noir",
        "name": "Film Noir Editorial",
        "category": "fashion-editorial",
        "prompt": "Film noir-inspired editorial. Black and white, high contrast. Subject in tailored black coat standing in rain-slicked alley. Single overhead streetlight providing hard directional light from above, casting long shadows. Wet surfaces reflecting light, creating environmental depth. Shot on Leica M11 with 35mm Summilux at f/2, slight motion blur on falling rain. Ilford HP5 Plus grain structure. Moody, mysterious, narrative tension — a still from an unmade film.",
        "tags": ["film-noir", "black-white", "rain", "dramatic", "editorial"],
        "source": "original",
    },
    {
        "id": "fashion_backstage",
        "name": "Backstage Fashion Show",
        "category": "fashion-editorial",
        "prompt": "Backstage at a fashion show. Makeup artists applying lipstick (only hands visible in frame). Subject wearing a corset decorated with beaded embroidery and crystals. Darkly lit backstage environment under the podium. Main emphasis on face and costume details. Camera flash emphasizing shine of beads and crystals on corset and shiny skin. Sensuality, luxury, glamour. Very detailed fabric texture, each bead individually rendered. Documentary editorial style capturing the chaos and beauty of preparation.",
        "tags": ["backstage", "fashion-show", "documentary", "luxury", "detail"],
        "source": "awesome-nanobanana-pro",
    },

    # --- PRODUCT ---
    {
        "id": "product_hero_minimal",
        "name": "Minimal Product Hero Shot",
        "category": "product",
        "prompt": "A stainless-steel product on a marble counter with subtle steam rising. Single product hero on seamless background. No visible logos, no hands, no camera reflections. Photorealistic with studio lighting setup. Shot on Canon R5 with RF 100mm f/2.8L Macro at f/4. Shallow depth of field isolating product. Rule of thirds composition. 4K resolution. Natural material interactions — metal reflections accurate, marble veining visible, steam behaving physically. Anti-aliased edges, low noise, high color depth. Professional commercial photography standard.",
        "tags": ["product", "minimal", "studio", "commercial", "hero-shot"],
        "source": "gemini-image-prompting-handbook",
    },
    {
        "id": "product_luxury_dark",
        "name": "Luxury Product Dark Mood",
        "category": "product",
        "prompt": "Luxury product photography on dark water surface. Product floating on dark reflective water with scattered flower petals. Deep black background with controlled spot lighting from above. Visible caustic light patterns from water surface. Crystal-clear reflections on water. Shot on Phase One IQ4 with 120mm macro lens. Ultra-sharp product detail, material textures rendered at microscopic level — metal brushing patterns, glass refractions, label printing texture. Rich deep shadows, selective highlights. Commercial fragrance photography aesthetic.",
        "tags": ["luxury", "dark", "water", "product", "fragrance"],
        "source": "awesome-nanobanana-pro",
    },
    {
        "id": "product_food_commercial",
        "name": "Commercial Food Photography",
        "category": "food-drink",
        "prompt": "Extreme close-up of a dish being plated, chef's hands visible at frame edge. Steam rising through backlight creating depth and warmth. Commercial food photography for advertising catalogue. Shot on Canon R5 with 100mm macro lens. Key light from behind and above creating rim highlights on steam and food textures. Fill light from front at low power preserving shadow depth. Visible food textures: crispy edges, glistening sauce, fresh herb leaves with water droplets. Color-accurate rendering for print reproduction. Shallow depth of field with in-focus hero element and soft background.",
        "tags": ["food", "commercial", "macro", "steam", "restaurant"],
        "source": "claude-prompts",
    },

    # --- ARCHITECTURE ---
    {
        "id": "arch_brutalist_moody",
        "name": "Brutalist Architecture Moody",
        "category": "architecture",
        "prompt": "Brutalist concrete building photographed in overcast light. Raw concrete texture with weathering stains and moss. Geometric repeating patterns of windows and structural elements. Shot on Nikon Z9 with 24mm f/1.8 S at f/8 for maximum sharpness throughout. Overcast sky providing even illumination revealing concrete texture without harsh shadows. Blue-gray color palette. Leading lines from structural geometry drawing eye through frame. Architectural photography precision — verticals corrected, no lens distortion. The beauty of raw material and pure form.",
        "tags": ["architecture", "brutalist", "concrete", "moody", "geometric"],
        "source": "original",
    },
    {
        "id": "arch_interior_natural_light",
        "name": "Interior Natural Light",
        "category": "architecture",
        "prompt": "Interior architectural photography of a minimalist space. Large windows providing soft directional natural light, creating long light shafts across clean surfaces. Warm wood and white plaster material palette. Shot on Fujifilm GFX 100S with 23mm wide angle at f/5.6. Golden hour light entering from left, casting warm geometric shadow patterns. Visible material textures — wood grain, plaster imperfections, stone floor patina. Clean composition with strong geometric lines. Architectural Digest quality.",
        "tags": ["interior", "architecture", "natural-light", "minimalist", "warm"],
        "source": "original",
    },

    # --- LANDSCAPE ---
    {
        "id": "landscape_documentary_street",
        "name": "Documentary Street Scene",
        "category": "street-documentary",
        "prompt": "An elderly man buying fruit at a small street market in late afternoon. Vendor handing change, man reaching. Urban street with bus stop and plastic bags. Shot on Sony A7 IV with 50mm f/1.4 GM at f/4. Medium depth of field keeping both figures and immediate environment sharp. Natural afternoon light with distance haze. Autumn atmosphere with dust particles. Kodak Portra rendering — muted warm tones, subtle grain. Rule of thirds composition with balanced subject placement. Photographic documentary quality, authentic textures, no posing, no direction. A real moment.",
        "tags": ["street", "documentary", "market", "candid", "portra"],
        "source": "gemini-image-prompting-handbook",
    },
    {
        "id": "landscape_stormy_coast",
        "name": "Stormy Coastal Portrait",
        "category": "landscape",
        "prompt": "A figure standing on a rainy pier with wind pulling their raincoat. Stormy coastline with lighthouse far behind. Waves crashing, sea spray visible. Shot on Canon R5 with 35mm f/1.4L at f/4. Dramatic lighting through storm clouds, muted desaturated color palette. Film grain texture. Authentic wet fabric draping, oxidized metal pier rails, weathered wood surfaces. Environmental atmosphere with mist, rain, and atmospheric depth. Golden hour light breaking through clouds on horizon. Cinematic framing, golden ratio composition. The raw beauty of human figure against elemental force.",
        "tags": ["landscape", "storm", "coastal", "dramatic", "cinematic"],
        "source": "gemini-image-prompting-handbook",
    },
    {
        "id": "landscape_golden_hour_vast",
        "name": "Golden Hour Vast Landscape",
        "category": "landscape",
        "prompt": "Vast landscape at golden hour, low sun casting extreme long shadows across rolling terrain. Warm light gradient from golden foreground to purple-blue distance. Shot on Fujifilm GFX 100S with 23mm wide-angle at f/11 for maximum depth of field. Fuji Velvia color rendering — vivid saturated greens, deep sky, punchy contrast. Expansive negative space composition, small human figure for scale at thirds intersection. Visible terrain texture — grass, rock, earth. Atmosphere with distance haze adding depth layers. Fine art landscape photography, large format print quality.",
        "tags": ["landscape", "golden-hour", "vast", "velvia", "fine-art"],
        "source": "original",
    },

    # --- CINEMATIC ---
    {
        "id": "cinematic_rainy_neon",
        "name": "Neon Rain Night Scene",
        "category": "street-documentary",
        "prompt": "Night street scene in rain. Neon signs reflecting in wet asphalt creating pools of colored light — red, blue, amber. Figure walking away from camera, umbrella silhouetted against neon glow. Shot on Sony A1 with 50mm f/1.2 GM wide open, shallow depth of field turning background lights into large colorful bokeh circles. CineStill 800T rendering — tungsten color balance, halation glow around neon highlights, orange-red halos on bright sources. Visible rain streaks in backlight. Atmospheric depth with mist diffusing distant lights. A frame from a Wong Kar-wai film that doesn't exist.",
        "tags": ["night", "rain", "neon", "cinestill", "cinematic", "bokeh"],
        "source": "original",
    },
    {
        "id": "cinematic_chiaroscuro_portrait",
        "name": "Chiaroscuro Cinematic Portrait",
        "category": "portrait",
        "prompt": "Chiaroscuro portrait inspired by Caravaggio and Gordon Willis. Single hard light source from upper camera-left, creating sharp defined shadows. Subject emerging from pure darkness, only one side of face illuminated. Shot on ARRI Alexa 35 with Zeiss Supreme Prime 50mm T1.5 wide open. Rich skin tones in the light, impenetrable shadows on the opposite side. Visible skin texture in highlights, no detail in shadows — intentional. 2.39:1 anamorphic crop. Color graded warm in highlights, cool in shadows. Cinematic tension in the gaze. A still from a film about someone with a secret.",
        "tags": ["chiaroscuro", "cinematic", "dramatic", "film", "portrait"],
        "source": "original",
    },
]
