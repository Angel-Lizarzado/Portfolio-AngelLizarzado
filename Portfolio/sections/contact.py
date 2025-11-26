import reflex as rx
from Portfolio.components.social_links import social_links
from Portfolio.utils import get_personal_data
from Portfolio.state import State

def contact_section() -> rx.Component:
    """
    Sección de contacto y footer con diseño mejorado.
    
    Returns:
        rx.Component: Sección de contacto/footer
    """
    # Cargar datos desde JSON
    data = get_personal_data()
    redes = data.get("redes_sociales", {})
    copyright_text = data.get("copyright", "© 2025")
    
    return rx.box(
        rx.container(
            rx.vstack(
                # Título principal
                rx.heading(
                    State.tr["contact"].to(dict)["title"],  # Traducido
                    size="5",
                    weight="bold",
                    style={
                        "background": "linear-gradient(90deg, cyan, purple)",
                        "-webkit-background-clip": "text",
                        "-webkit-text-fill-color": "transparent",
                        "word-wrap": "break-word",
                    },
                    text_align="center",
                ),
                
                # Descripción
                rx.box(
                    rx.text(
                        State.tr["contact"].to(dict)["description"],  # Traducido
                        size="2",
                        color="gray",
                        text_align="center",
                        style={
                            "word-wrap": "break-word",
                            "overflow-wrap": "break-word",
                            "white-space": "normal",
                            "max-width": "90%",  # Fuerza el wrap
                            "margin": "0 auto",  # Centra el texto
                        },
                    ),
                    width="100%",
                    padding_x="4",
                ),
                
                # Enlaces sociales
                rx.vstack(
                    social_links(
                        github=redes.get("github"),
                        linkedin=redes.get("linkedin"),
                        email=redes.get("email"),
                        twitter=redes.get("twitter"),
                    ),
                    spacing="4",
                    padding_y="6",
                ),
                
                # Divider
                rx.divider(width="100%", margin_y="6"),
                
                # Footer - Desktop (horizontal)
                rx.hstack(
                    rx.text(copyright_text, size="2", color="gray"),
                    rx.spacer(),
                    rx.hstack(
                        rx.text(State.tr["contact"].to(dict)["footer_built_with"], size="2", color="gray"),  # Traducido
                        rx.link(
                            rx.text("🐍 Python", size="2", weight="bold"),
                            href="https://www.python.org/",
                            style={"text-decoration": "none"},
                            _hover={"color": "cyan"},
                        ),
                        rx.text("+", size="2", color="gray"),
                        rx.link(
                            rx.text("⚡ Reflex", size="2", weight="bold"),
                            href="https://reflex.dev/",
                            style={"text-decoration": "none"},
                            _hover={"color": "purple"},
                        ),
                        spacing="2",
                    ),
                    width="100%",
                    align_items="center",
                    display=["none", "none", "flex"],  # Solo desktop
                ),
                
                # Footer - Mobile (vertical stack)
                rx.vstack(
                    rx.text(copyright_text, size="2", color="gray", text_align="center"),
                    rx.hstack(
                        rx.text(State.tr["contact"].to(dict)["footer_built_with"], size="2", color="gray"),  # Traducido
                        rx.link(
                            rx.text("🐍 Python", size="2", weight="bold"),
                            href="https://www.python.org/",
                            style={"text-decoration": "none"},
                            _hover={"color": "cyan"},
                        ),
                        rx.text("+", size="2", color="gray"),
                        rx.link(
                            rx.text("⚡ Reflex", size="2", weight="bold"),
                            href="https://reflex.dev/",
                            style={"text-decoration": "none"},
                            _hover={"color": "purple"},
                        ),
                        spacing="1",
                        flex_wrap="wrap",
                        justify="center",
                    ),
                    spacing="2",
                    width="100%",
                    align_items="center",
                    display=["flex", "flex", "none"],  # Solo móvil/tabla
                ),
                
                spacing="6",
                align_items="center",
                width="100%",  # Importante: ancho completo
                padding_y="12",
            ),
            max_width="1200px",
            padding_x="4",  # Márgenes laterales importantes para móvil
        ),
        width="100%",
        style={
            "background": "linear-gradient(to bottom, transparent, var(--gray-2))",
            "border-top": "1px solid var(--gray-5)",
            "display": "flex",
            "justify-content": "center",
        },
    )
