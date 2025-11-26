import reflex as rx
from Portfolio.components.project_card import project_card
from Portfolio.components.skeleton import skeleton_projects_section
from Portfolio.utils import get_projects_data
from Portfolio.state import State

def projects_section() -> rx.Component:
    """
    Sección de proyectos destacados.
    
    Returns:
        rx.Component: Grid de proyectos
    """
    # Cargar proyectos desde JSON
    projects = get_projects_data()
    
    return rx.cond(
        State.is_loading,
        skeleton_projects_section(),
        rx.vstack(
            # Título principal
            rx.center(
                rx.heading(
                    State.tr["projects"].to(dict)["title"],  # Traducido
                    size="6",  # Reducido de 8 a 6
                    weight="bold",
                ),
                width="100%",
                margin_bottom="6",
            ),
            
            rx.grid(
                *[
                    project_card(
                        title=p["titulo"],
                        description=rx.cond(
                            State.current_language == "es",
                            p["descripcion_es"],
                            p["descripcion_en"]
                        ),
                        technologies=p["tecnologias"],
                        github_url=p.get("github_url"),
                        demo_url=p.get("demo_url"),
                        image_url=p.get("imagen_url"),
                        bg_color=p.get("bg_color"),
                    )
                    for p in projects
                ],
                columns=rx.breakpoints(initial="1", sm="1", md="2", lg="3"),  # Responsive: 1 col móvil, 2 tablet, 3 desktop
                spacing="6",
                width="100%",
            ),
            
            spacing="3",
            align_items="center",
            width="100%",
            class_name="fade-in",
        )
    )
