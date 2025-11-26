import reflex as rx
import json
import os
import asyncio
from Portfolio.utils.i18n import TRANSLATIONS_DIR

def load_all_translations():
    """Load all translation files into a dictionary"""
    data = {}
    for lang in ["es", "en"]:
        try:
            with open(os.path.join(TRANSLATIONS_DIR, f"{lang}.json"), "r", encoding="utf-8") as f:
                data[lang] = json.load(f)
        except Exception as e:
            print(f"Error loading translations for {lang}: {e}")
            data[lang] = {}
    return data

class State(rx.State):
    """The app state."""
    
    # Language state
    current_language: str = "es"
    
    # Loading state
    is_loading: bool = True
    
    def set_initial_language(self, lang: str):
        """Set the initial language from client side"""
        if lang in ["es", "en"]:
            self.current_language = lang

    async def on_load(self):
        """Simulate data loading and detect language"""
        await asyncio.sleep(1.0)  # 1 segundo de carga simulada
        self.is_loading = False
        
        # Detectar idioma del navegador si no hay preferencia guardada
        return rx.call_script(
            """
            (function() {
                const saved = localStorage.getItem('language');
                if (saved) return saved;
                const browser = navigator.language || navigator.userLanguage;
                return browser.startsWith('en') ? 'en' : 'es';
            })()
            """,
            callback=State.set_initial_language
        )
    
    # Store all translations
    _translations: dict = load_all_translations()
    
    @rx.var
    def tr(self) -> dict:
        """Get translations for current language"""
        return self._translations.get(self.current_language, self._translations.get("es", {}))
    
    # Theme persistence
    def toggle_theme(self):
        """Toggle between light and dark mode and save to localStorage"""
        return rx.call_script(
            """
            // Toggle color mode
            const currentMode = document.documentElement.classList.contains('dark') ? 'light' : 'dark';
            
            if (currentMode === 'dark') {
                document.documentElement.classList.add('dark');
                localStorage.setItem('theme', 'dark');
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('theme', 'light');
            }
            """
        )
    
    def toggle_language(self):
        """Toggle between Spanish and English"""
        new_lang = "en" if self.current_language == "es" else "es"
        self.current_language = new_lang
        return rx.call_script(f"localStorage.setItem('language', '{new_lang}');")
    
    def load_language(self):
        """Load saved language from localStorage"""
        return rx.call_script(
            """
            const savedLang = localStorage.getItem('language') || 'es';
            return savedLang;
            """
        )
