import json
import os
from deep_translator import GoogleTranslator
from typing import List, Dict, Union

# Configuración
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")

def translate_text(text: str) -> str:
    """Traduce texto de español a inglés usando Google Translate"""
    if not text:
        return ""
    try:
        translator = GoogleTranslator(source='es', target='en')
        return translator.translate(text)
    except Exception as e:
        print(f"Error traduciendo '{text[:20]}...': {e}")
        return text

def process_projects():
    """Procesa y traduce projects.json"""
    filepath = os.path.join(DATA_DIR, "projects.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for project in data.get("proyectos", []):
        # Traducir descripción
        if "descripcion" in project and isinstance(project["descripcion"], str):
            print(f"Traduciendo proyecto: {project.get('titulo', 'Sin título')}")
            project["descripcion_es"] = project["descripcion"]
            project["descripcion_en"] = translate_text(project["descripcion"])
            del project["descripcion"] # Eliminar campo antiguo
            modified = True
            
        # Si ya tiene descripcion_es pero falta en, traducir
        elif "descripcion_es" in project and "descripcion_en" not in project:
            print(f"Traduciendo proyecto (falta EN): {project.get('titulo', 'Sin título')}")
            project["descripcion_en"] = translate_text(project["descripcion_es"])
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("projects.json actualizado.")
    else:
        print("No hubo cambios en projects.json")

def process_experience():
    """Procesa y traduce experience.json"""
    filepath = os.path.join(DATA_DIR, "experience.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    
    # 1. Educación
    for edu in data.get("educacion", []):
        # Traducir programa
        if "programa" in edu and isinstance(edu["programa"], str):
            print(f"Traduciendo educación: {edu.get('institucion', 'Sin inst')}")
            edu["programa_es"] = edu["programa"]
            edu["programa_en"] = translate_text(edu["programa"])
            del edu["programa"]
            modified = True
            
    # 2. Experiencia (Lista de strings -> Lista de objetos)
    new_experience = []
    for item in data.get("experiencia", []):
        if isinstance(item, str):
            print(f"Traduciendo experiencia: {item[:20]}...")
            new_experience.append({
                "es": item,
                "en": translate_text(item)
            })
            modified = True
        elif isinstance(item, dict) and "es" in item and "en" not in item:
             item["en"] = translate_text(item["es"])
             new_experience.append(item)
             modified = True
        else:
            new_experience.append(item)
            
    if modified:
        data["experiencia"] = new_experience
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("experience.json actualizado.")
    else:
        print("No hubo cambios en experience.json")

if __name__ == "__main__":
    print("Iniciando traducción automática...")
    process_projects()
    process_experience()
    print("¡Proceso completado!")
