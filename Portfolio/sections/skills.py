import reflex as rx
from Portfolio.components.skill_badge import skill_badge
from Portfolio.components.skeleton import skeleton_skills_section
from Portfolio.utils import get_skills_data
from Portfolio.state import State

def skills_section() -> rx.Component:
    """
    Sección de habilidades técnicas categorizadas.
    
    Returns:
        rx.Component: Sección completa de skills
    """
    # Cargar skills desde JSON
    skills_data = get_skills_data()
    categorias = skills_data.get("categorias", [])
    
    # Crear componentes de categorías dinámicamente
    category_components = []
    for categoria in categorias:
        category_components.append(
            rx.vstack(
                rx.heading(
                    State.tr["skills"].to(dict)["categories"].to(dict)[categoria["nombre"]],  # Traducido
                    size="4",  # Reducido de 5 a 4
                    color="cyan",
                    margin_bottom="3",
                ),
                rx.flex(
                    *[skill_badge(tech) for tech in categoria["tecnologias"]],
                    spacing="3",
                    wrap="wrap",
                    justify="start",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            )
        )
    
    return rx.cond(
        State.is_loading,
        skeleton_skills_section(),
        rx.vstack(
            # Título principal
            rx.center(
                rx.heading(
                    State.tr["skills"].to(dict)["title"],  # Traducido
                    size="6",  # Reducido de 8 a 6
                    weight="bold",
                ),
                width="100%",
                margin_bottom="6",
            ),
            
            *category_components,
            
            spacing="7",
            align_items="start",
            width="100%",
            class_name="fade-in",
        )
    )
