import reflex as rx
from Portfolio.utils import get_personal_data
from Portfolio.state import State

def about_section() -> rx.Component:
    """Sección Sobre Mi del portfolio"""
    # Cargar datos desde JSON
    data = get_personal_data()
    
    return rx.vstack(
        rx.center(
            rx.heading(
                State.tr["about"].to(dict)["title"],  # Traducido
                size="6",  # Reducido de 8 a 6
                weight="bold",
            ),
            width="100%",
            margin_bottom="6",
        ),
        
        rx.center(
            rx.vstack(
                rx.foreach(
                    State.tr["about"].to(dict)["paragraphs"].to(list),
                    lambda paragraph: rx.text(
                        paragraph,
                        size="3",  # Reducido de 4 a 3 para móvil
                        line_height="1.8",
                    )
                ),
                spacing="5",
                max_width="900px",
                style={
                    "text-align": "center",
                },
            ),
            width="100%",
        ),
        
        spacing="0",
        align_items="center",
        width="100%",
    )