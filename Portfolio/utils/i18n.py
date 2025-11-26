"""Internationalization utilities for multi-language support"""

import json
import os
from typing import Dict, Any

# Directory for translation files
TRANSLATIONS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "translations"
)

# Cache for loaded translations
_translations_cache: Dict[str, Dict[str, Any]] = {}


def load_translations(lang: str = "es") -> Dict[str, Any]:
    """
    Load translations for specified language
    
    Args:
        lang: Language code ('es' or 'en')
    
    Returns:
        dict: Translations dictionary
    """
    if lang in _translations_cache:
        return _translations_cache[lang]
    
    file_path = os.path.join(TRANSLATIONS_DIR, f"{lang}.json")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            translations = json.load(f)
            _translations_cache[lang] = translations
            return translations
    except FileNotFoundError:
        # Fallback to Spanish if language not found
        if lang != "es":
            return load_translations("es")
        raise


def get_text(key_path: str, lang: str = "es", **kwargs) -> str:
    """
    Get translated text by key path
    
    Args:
        key_path: Dot-separated path to translation key (e.g., 'navbar.links.home')
        lang: Language code
        **kwargs: Variables to replace in template (e.g., name="John")
    
    Returns:
        str: Translated text
    
    Example:
        >>> get_text('hero.subtitle', lang='en', title='Developer')
        'Developer'
    """
    translations = load_translations(lang)
    keys = key_path.split('.')
    
    value = translations
    for key in keys:
        value = value.get(key, "")
        if not value:
            return key_path  # Return key if not found
    
    # Replace template variables
    if isinstance(value, str) and kwargs:
        for k, v in kwargs.items():
            value = value.replace(f"{{{{{k}}}}}", str(v))
    
    return value
