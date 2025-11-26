import reflex as rx
from Portfolio.components.skill_badge import skill_badge
from Portfolio.utils import get_personal_data
from Portfolio.state import State

def hero_section() -> rx.Component:
    """Sección Hero principal del portfolio - Responsive"""
    # Cargar datos personales desde JSON
    data = get_personal_data()
    
    return rx.center(
        rx.vstack(
            # Contenido principal
            rx.vstack(
                rx.heading(
                    data["nombre"],
                    size="7",  # Reducido de 9 a 7 para móvil
                    weight="bold",
                    style={
                        "background": "linear-gradient(90deg, cyan, purple)",
                        "-webkit-background-clip": "text",
                        "-webkit-text-fill-color": "transparent",
                        "word-wrap": "break-word",
                        "overflow-wrap": "break-word",
                    },
                    text_align="center",
                ),
                rx.box(
                    rx.avatar(
                        fallback=data["iniciales"],
                        size="9",
                        radius="full",
                        style={
                            "border": "solid 3px cyan",
                            "box-shadow": "0 8px 32px rgba(0, 200, 255, 0.3)",
                            "transition": "all 0.3s ease",
                        },
                        _hover={
                            "transform": "scale(1.05)",
                            "box-shadow": "0 12px 48px rgba(0, 200, 255, 0.5)",
                        },
                    ),
                    margin_y="6",
                ),
                rx.text(
                    State.tr["hero"].to(dict)["role"],  # Traducido
                    size="4",  # Reducido de 5 a 4
                    weight="medium",
                    color="gray",
                    text_align="center",
                ),
                rx.text(
                    State.tr["hero"].to(dict)["description"],  # Traducido
                    size="3",  # Reducido de 4 a 3
                    color="gray",
                    max_width="600px",
                    text_align="center",
                ),
                
                # Botón Descargar CV
                rx.link(
                    rx.button(
                        rx.icon("download", size=18),
                        State.tr["hero"].to(dict)["download_cv"],  # Traducido
                        size="3",
                        variant="outline",
                        color_scheme="cyan",
                        radius="full",
                        style={
                            "border-width": "2px",
                            "transition": "all 0.3s ease",
                        },
                        _hover={
                            "transform": "translateY(-2px)",
                            "box-shadow": "0 4px 12px rgba(0, 200, 255, 0.3)",
                            "background": "rgba(0, 200, 255, 0.1)",
                        },
                    ),
                    href="/assets/cv.pdf",
                    is_external=True,
                    style={"text-decoration": "none"},
                ),

                # Tecnologías usando componente reutilizable y datos JSON
                rx.flex(
                    *[skill_badge(tech) for tech in data["tecnologias_principales"]],
                    spacing="2",
                    wrap="wrap",
                    max_width="600px",
                    justify="center",
                ),
                spacing="5",
                align_items="center",
                width="100%",
            ),
            
            spacing="6",
            width="100%",
            align_items="center",
            padding_y="8",
        ),
        width="100%",
    )