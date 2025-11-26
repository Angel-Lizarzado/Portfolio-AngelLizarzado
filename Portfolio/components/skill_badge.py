import reflex as rx

# Diccionario de colores predefinidos para tecnologías comunes
TECH_COLORS = {
    "Python": {"bg": "#3776AB", "text": "white"},
    "Javascript": {"bg": "#F7DF1E", "text": "black"},
    "JavaScript": {"bg": "#F7DF1E", "text": "black"},
    "Typescript": {"bg": "#3178C6", "text": "white"},
    "TypeScript": {"bg": "#3178C6", "text": "white"},
    "PHP": {"bg": "#777BB4", "text": "white"},
    "Node.js": {"bg": "#339933", "text": "white"},
    "React": {"bg": "#61DAFB", "text": "black"},
    "Next.js": {"bg": "#000000", "text": "white"},
    "Vue": {"bg": "#42B883", "text": "white"},
    "Angular": {"bg": "#DD0031", "text": "white"},
    "Django": {"bg": "#092E20", "text": "white"},
    "Flask": {"bg": "#000000", "text": "white"},
    "FastAPI": {"bg": "#009688", "text": "white"},
    "HTML": {"bg": "#E34F26", "text": "white"},
    "HTML5": {"bg": "#E34F26", "text": "white"},
    "CSS": {"bg": "#1572B6", "text": "white"},
    "CSS3": {"bg": "#1572B6", "text": "white"},
    "TailwindCSS": {"bg": "#06B6D4", "text": "white"},
    "Bootstrap": {"bg": "#7952B3", "text": "white"},
    "Git": {"bg": "#F05032", "text": "white"},
    "GitHub": {"bg": "#181717", "text": "white"},
    "Docker": {"bg": "#2496ED", "text": "white"},
    "AWS": {"bg": "#FF9900", "text": "black"},
    "Linux": {"bg": "#FCC624", "text": "black"},
    "Windows Server": {"bg": "#0078D7", "text": "white"},
    "SQL": {"bg": "#003B57", "text": "white"},
    "PostgreSQL": {"bg": "#336791", "text": "white"},
    "MongoDB": {"bg": "#47A248", "text": "white"},
    "MySQL": {"bg": "#4479A1", "text": "white"},
    "Redis": {"bg": "#DC382D", "text": "white"},
    "GraphQL": {"bg": "#E10098", "text": "white"},
    "REST API": {"bg": "#009688", "text": "white"},
    "REST APIs": {"bg": "#009688", "text": "white"},
    "VS Code": {"bg": "#007ACC", "text": "white"},
    "Postman": {"bg": "#FF6C37", "text": "white"},
    "Testing": {"bg": "#699F4C", "text": "white"},
    "Reflex": {"bg": "#5646ED", "text": "white"},
}

def skill_badge(
    name: str,
    background_color: str = None,
    text_color: str = None,
    variant: str = "solid",
    size: str = "2",
) -> rx.Component:
    """
    Componente reutilizable para badges de habilidades/tecnologías.
    
    Args:
        name: Nombre de la tecnología
        background_color: Color de fondo (opcional, usa predefinido si existe)
        text_color: Color del texto (opcional, usa predefinido si existe)
        variant: Variante del badge ("solid", "soft", "outline")
        size: Tamaño del badge ("1", "2", "3")
    
    Returns:
        rx.Component: Badge con efectos hover
    """
    # Usar colores predefinidos si existen y no se especificaron manualmente
    if name in TECH_COLORS and background_color is None:
        bg_color = TECH_COLORS[name]["bg"]
        txt_color = TECH_COLORS[name]["text"]
    else:
        bg_color = background_color or "#6B7280"  # Color gris por defecto
        txt_color = text_color or "white"
    
    return rx.badge(
        name,
        background_color=bg_color,
        color=txt_color,
        variant=variant,
        size=size,
        style={
            "transition": "all 0.3s ease",
            "cursor": "default",
        },
        _hover={
            "box_shadow": "0 4px 12px rgba(0, 0, 0, 0.15)",
            "transform": "translateY(-2px)",
        },
    )
