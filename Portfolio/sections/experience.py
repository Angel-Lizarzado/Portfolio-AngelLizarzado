import reflex as rx
from Portfolio.components.card_component import custom_card
from Portfolio.components.skeleton import skeleton_experience_section
from Portfolio.utils import get_experience_data
from Portfolio.state import State

def experience_section() -> rx.Component:
    """Sección de Educación y Experiencia del portfolio"""
    # Cargar datos desde JSON
    exp_data = get_experience_data()
    educacion = exp_data.get("educacion", [])
    experiencia = exp_data.get("experiencia", [])
    
    # Crear cards de educación dinámicamente
    education_cards = []
    for edu in educacion:
        education_cards.append(
            custom_card(
                rx.hstack(
                    rx.image(
                        src=edu["logo_url"],
                        width="6em",
                        height="6em",
                        border_radius="md",
                    ),
                    rx.vstack(
                        rx.text(
                            edu["institucion"],
                            font_style="italic",
                            weight="medium",
                        ),
                        rx.text(
                            rx.cond(
                                State.current_language == "es",
                                edu["programa_es"],
                                edu["programa_en"]
                            ),
                            weight="bold",
                        ),
                        rx.text(
                            edu["periodo"],
                            font_style="italic",
                            size="2",
                            color="gray",
                        ),
                        spacing="2",
                        align_items="start",
                    ),
                    spacing="4",
                    align_items="center",
                ),
                hover_border_color="cyan",
            )
        )
    
    # Crear lista de experiencia dinámicamente
    experience_items = [
        rx.text(
            rx.cond(
                State.current_language == "es",
                item["es"],
                item["en"]
            ),
            size="3"
        )
        for item in experiencia
    ]
    
    return rx.cond(
        State.is_loading,
        skeleton_experience_section(),
        rx.vstack(
            rx.center(
                rx.heading(State.tr["experience"].to(dict)["title"], size="6", weight="bold"),  # Traducido
                width="100%",
                margin_bottom="6",
            ),
            
            rx.grid(
                # Columna izquierda - Educación
                rx.vstack(
                    rx.heading(State.tr["experience"].to(dict)["education_title"], size="5", color="cyan"),  # Traducido
                    *education_cards,
                    spacing="4",
                    align_items="start",
                    width="100%",
                ),
                
                # Columna derecha - Experiencia
                rx.vstack(
                    rx.heading(State.tr["experience"].to(dict)["experience_title"], size="5", color="cyan"),  # Traducido
                    rx.vstack(
                        *experience_items,
                        spacing="3",
                        align_items="start",
                    ),
                    spacing="4",
                    align_items="start",
                    width="100%",
                ),
                
                columns=rx.breakpoints(initial="1", md="2"),  # 1 columna en móvil, 2 en desktop
                spacing="8",
                width="100%",
            ),
            
            spacing="3",
            align_items="center",
            width="100%",
            class_name="fade-in",
        )
    )
