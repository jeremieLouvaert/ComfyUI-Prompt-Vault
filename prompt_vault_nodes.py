"""
ComfyUI Prompt Vault — Photographic prompt arsenal for high-end image generation.

Two nodes:
  - Prompt Vault Browse: Filter, pick, and edit from curated template library
  - Prompt Vault Build: Assemble prompts from photographic components (camera, lighting, film, mood)
"""

import os
import json
import hashlib

try:
    import folder_paths
except ImportError:
    folder_paths = None

from .vault_data import (
    CAMERAS, LIGHTING, FILM_STOCKS, MOODS,
    QUALITY_DIRECTIVES, COMPOSITIONS, CATEGORIES, TEMPLATES,
)

CATEGORY = "AKURATE/Prompt Vault"

# ---------------------------------------------------------------------------
# FAVORITES PERSISTENCE
# ---------------------------------------------------------------------------

def _favorites_path():
    if folder_paths:
        root = os.path.dirname(folder_paths.get_output_directory())
    else:
        root = os.path.dirname(__file__)
    return os.path.join(root, "prompt_vault_favorites.json")


def _load_favorites():
    path = _favorites_path()
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []


def _save_favorite(prompt_text, source="custom"):
    favorites = _load_favorites()
    entry = {
        "id": hashlib.sha256(prompt_text.encode()).hexdigest()[:12],
        "prompt": prompt_text,
        "source": source,
    }
    # Deduplicate
    if not any(f["id"] == entry["id"] for f in favorites):
        favorites.append(entry)
        try:
            with open(_favorites_path(), "w", encoding="utf-8") as f:
                json.dump(favorites, f, indent=2, ensure_ascii=False)
            print(f"[Prompt Vault] Saved to favorites ({len(favorites)} total)")
        except Exception as e:
            print(f"[Prompt Vault] Failed to save favorite: {e}")


# ---------------------------------------------------------------------------
# NODE: Prompt Vault Browse
# ---------------------------------------------------------------------------

class PromptVaultBrowse:
    """Browse, filter, and edit prompts from the curated template library."""

    @classmethod
    def INPUT_TYPES(cls):
        # Build template list per category
        all_names = ["-- select a template --"]
        for t in TEMPLATES:
            all_names.append(f"[{t['category']}] {t['name']}")

        categories_with_all = ["all"] + CATEGORIES

        return {
            "required": {
                "category_filter": (categories_with_all, {"default": "all"}),
                "template": (all_names, {"default": all_names[0]}),
                "edit_prompt": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Selected template appears here. Edit freely before output.",
                }),
            },
            "optional": {
                "save_to_favorites": ("BOOLEAN", {"default": False}),
                "append_text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Additional text appended to the prompt...",
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("prompt", "prompt_dna",)
    FUNCTION = "browse"
    CATEGORY = CATEGORY

    def browse(self, category_filter, template, edit_prompt,
               save_to_favorites=False, append_text=""):

        # If user selected a template and edit_prompt is empty, load the template
        final_prompt = edit_prompt.strip()

        if not final_prompt and template != "-- select a template --":
            # Find the template
            for t in TEMPLATES:
                display = f"[{t['category']}] {t['name']}"
                if display == template:
                    final_prompt = t["prompt"]
                    break

        if not final_prompt:
            # Show available templates for the selected category
            available = TEMPLATES if category_filter == "all" else [
                t for t in TEMPLATES if t["category"] == category_filter
            ]
            listing = "\n".join(
                f"  [{t['category']}] {t['name']}: {t['prompt'][:80]}..."
                for t in available
            )
            return (f"No template selected. Available ({len(available)}):\n{listing}",
                    json.dumps({"status": "no_selection", "available": len(available)}))

        # Append extra text
        if append_text.strip():
            final_prompt = final_prompt + " " + append_text.strip()

        # Save to favorites
        if save_to_favorites:
            _save_favorite(final_prompt, source="browse")

        # Build DNA
        dna = {
            "source": "browse",
            "template": template,
            "category_filter": category_filter,
            "edited": edit_prompt.strip() != "",
            "char_count": len(final_prompt),
        }

        print(f"[Prompt Vault] Browse output: {final_prompt[:80]}...")
        return (final_prompt, json.dumps(dna, indent=2),)


# ---------------------------------------------------------------------------
# NODE: Prompt Vault Build
# ---------------------------------------------------------------------------

class PromptVaultBuild:
    """Assemble prompts from photographic components."""

    @classmethod
    def INPUT_TYPES(cls):
        camera_list = ["none"] + list(CAMERAS.keys())
        lighting_list = ["none"] + list(LIGHTING.keys())
        film_list = ["none"] + list(FILM_STOCKS.keys())
        mood_list = ["none"] + list(MOODS.keys())
        quality_list = ["none"] + list(QUALITY_DIRECTIVES.keys())
        composition_list = ["none"] + list(COMPOSITIONS.keys())

        return {
            "required": {
                "subject": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Describe your subject and scene...",
                }),
                "camera_lens": (camera_list, {"default": camera_list[0]}),
                "lighting": (lighting_list, {"default": lighting_list[0]}),
                "film_stock": (film_list, {"default": film_list[0]}),
                "mood": (mood_list, {"default": mood_list[0]}),
                "quality_directive": (quality_list, {"default": "Ultra-realism (anti-AI)"}),
                "composition": (composition_list, {"default": composition_list[0]}),
            },
            "optional": {
                "extra_details": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Additional specific details...",
                }),
                "save_to_favorites": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("prompt", "prompt_dna",)
    FUNCTION = "build"
    CATEGORY = CATEGORY

    def build(self, subject, camera_lens, lighting, film_stock, mood,
              quality_directive, composition, extra_details="", save_to_favorites=False):

        if not subject.strip():
            return ("Error: Subject description is required.",
                    json.dumps({"error": "no_subject"}))

        # Assemble the prompt from components
        parts = [subject.strip()]

        components_used = {"subject": subject.strip()}

        if camera_lens != "none":
            parts.append(CAMERAS[camera_lens])
            components_used["camera_lens"] = camera_lens

        if lighting != "none":
            parts.append(LIGHTING[lighting])
            components_used["lighting"] = lighting

        if film_stock != "none":
            parts.append(FILM_STOCKS[film_stock])
            components_used["film_stock"] = film_stock

        if mood != "none":
            parts.append(MOODS[mood])
            components_used["mood"] = mood

        if composition != "none":
            parts.append(COMPOSITIONS[composition])
            components_used["composition"] = composition

        if quality_directive != "none":
            parts.append(QUALITY_DIRECTIVES[quality_directive])
            components_used["quality_directive"] = quality_directive

        if extra_details.strip():
            parts.append(extra_details.strip())
            components_used["extra_details"] = extra_details.strip()

        final_prompt = ". ".join(parts)

        # Save to favorites
        if save_to_favorites:
            _save_favorite(final_prompt, source="build")

        # Build DNA — full recipe for reproducibility
        dna = {
            "source": "build",
            "components": components_used,
            "component_count": len(components_used),
            "char_count": len(final_prompt),
        }

        print(f"[Prompt Vault] Built prompt from {len(components_used)} components ({len(final_prompt)} chars)")
        return (final_prompt, json.dumps(dna, indent=2),)


# ---------------------------------------------------------------------------
# NODE: Prompt Vault Favorites
# ---------------------------------------------------------------------------

class PromptVaultFavorites:
    """Load and manage saved favorite prompts."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "action": (["list", "load_latest", "clear_all"], {"default": "list"}),
            },
            "optional": {
                "favorite_index": ("INT", {
                    "default": 0, "min": 0, "max": 999,
                    "tooltip": "Index of the favorite to load (0 = most recent)",
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("prompt", "info",)
    FUNCTION = "manage"
    CATEGORY = CATEGORY

    def manage(self, action, favorite_index=0):
        favorites = _load_favorites()

        if action == "clear_all":
            try:
                path = _favorites_path()
                if os.path.exists(path):
                    os.remove(path)
                return ("Favorites cleared.", f"Deleted {len(favorites)} favorites.")
            except Exception as e:
                return ("", f"Error: {e}")

        if not favorites:
            return ("No favorites saved yet.", "Use 'save_to_favorites' on Browse or Build nodes.")

        if action == "list":
            lines = [f"=== Prompt Vault Favorites ({len(favorites)}) ===", ""]
            for i, fav in enumerate(reversed(favorites)):
                lines.append(f"[{i}] ({fav.get('source', '?')}) {fav['prompt'][:100]}...")
            return ("\n".join(lines), f"{len(favorites)} favorites stored")

        if action == "load_latest":
            idx = min(favorite_index, len(favorites) - 1)
            fav = list(reversed(favorites))[idx]
            return (fav["prompt"], f"Loaded favorite #{idx} ({fav.get('source', '?')})")

        return ("", "Unknown action")


# ---------------------------------------------------------------------------
# MAPPINGS
# ---------------------------------------------------------------------------

NODE_CLASS_MAPPINGS = {
    "PromptVaultBrowse": PromptVaultBrowse,
    "PromptVaultBuild": PromptVaultBuild,
    "PromptVaultFavorites": PromptVaultFavorites,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptVaultBrowse": "Prompt Vault — Browse",
    "PromptVaultBuild": "Prompt Vault — Build",
    "PromptVaultFavorites": "Prompt Vault — Favorites",
}
