"""Utilidades para cargar datos desde archivos JSON"""

import json
import os

# Directorio base de datos - ruta relativa desde el proyecto
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")


def load_json(filename: str) -> dict:
    """
    Carga un archivo JSON desde el directorio data/
    
    Args:
        filename: Nombre del archivo JSON (ej: 'personal.json')
    
    Returns:
        dict: Datos del archivo JSON
    """
    file_path = os.path.join(DATA_DIR, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_personal_data() -> dict:
    """Obtiene datos personales del portfolio"""
    return load_json('personal.json')


def get_skills_data() -> dict:
    """Obtiene datos de habilidades técnicas"""
    return load_json('skills.json')


def get_projects_data() -> list:
    """Obtiene lista de proyectos"""
    data = load_json('projects.json')
    return data.get('proyectos', [])


def get_experience_data() -> dict:
    """Obtiene datos de experiencia y educación"""
    return load_json('experience.json')
