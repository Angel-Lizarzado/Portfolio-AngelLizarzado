import reflex as rx
from Portfolio.state import State

class NavbarState(rx.State):
    """Estado para el menú hamburguesa"""
    menu_open: bool = False
    
    def toggle_menu(self):
        """Toggle del menú móvil"""
        self.menu_open = not self.menu_open


def navbar() -> rx.Component:
    """Navbar responsive con menú hamburguesa en móvil"""
    
    nav_links = [
        ("Inicio", "#inicio"),
        ("Sobre Mí", "#sobre-mi"),
        ("Skills", "#skills"),
        ("Experiencia", "#experiencia"),
        ("Proyectos", "#proyectos"),
        ("Contacto", "#contacto"),
    ]
    
    return rx.box(
        rx.flex(
            # Logo/Nombre
            rx.link(
                rx.heading(
                    "AL",
                    size="6",
                    style={
                        "font-weight": "900",
                        "background": "linear-gradient(90deg, cyan, purple)",
                        "-webkit-background-clip": "text",
                        "-webkit-text-fill-color": "transparent",
                        "cursor": "pointer",
                    },
                ),
                href="#inicio",
            ),
            
            # Links desktop (ocultos en móvil)
            rx.box(
                rx.hstack(
                    *[
                        rx.link(
                            rx.text(text, size="2", weight="medium"),
                            href=href,
                            style={
                                "transition": "all 0.2s ease",
                                "text-decoration": "none",
                                "padding": "0.5em 1em",
                                "border-radius": "9999px",
                            },
                            _hover={
                                "color": "cyan",
                                "background": "rgba(255, 255, 255, 0.05)",
                            },
                        )
                        for text, href in nav_links
                    ],
                    spacing="2",  # Reducido porque ahora tienen padding
                ),
                display=["none", "none", "block"],  # Oculto en móvil
            ),
            
            # Botón hamburguesa (solo móvil)
            rx.box(
                rx.icon_button(
                    rx.icon("menu", size=24),
                    on_click=NavbarState.toggle_menu,
                    variant="ghost",
                    size="3",
                    style={"cursor": "pointer"},
                ),
                display=["block", "block", "none"],
            ),
            
            rx.hstack(
                # Botón de idioma
                rx.button(
                    rx.cond(
                        State.current_language == "es",
                        rx.text("ES", size="3", weight="bold"),
                        rx.text("EN", size="3", weight="bold"),
                    ),
                    on_click=State.toggle_language,
                    variant="ghost",
                    size="3",
                    padding="2",
                    style={"cursor": "pointer"},
                ),
                
                # Botón de dark mode
                rx.color_mode.button(),
                
                spacing="2",
                align_items="center",
            ),
            
            width="100%",
            max_width="1200px",
            margin_x="auto",
            align_items="center",
            justify="center",
            style={"gap": "4rem"},  # Espaciado personalizado (spacing max es 9)
            padding_y="4",
            padding_x="4",
        ),
        
        # Menú móvil desplegable - OVERLAY con blur
        rx.cond(
            NavbarState.menu_open,
            rx.box(
                rx.vstack(
                    *[
                        rx.link(
                            rx.text(text, size="4", weight="medium"),
                            href=href,
                            on_click=NavbarState.toggle_menu,  # Cerrar al hacer click
                            style={
                                "transition": "all 0.2s ease",
                                "text-decoration": "none",
                                "width": "100%",
                                "padding": "16px",
                                "border-radius": "8px",
                            },
                            _hover={
                                "background": "var(--gray-4)",
                                "color": "cyan",
                            },
                        )
                        for text, href in nav_links
                    ],
                    spacing="1",
                    padding="6",
                    width="100%",
                ),
                style={
                    "position": "absolute",
                    "top": "100%",
                    "left": "0",
                    "right": "0",
                    "background": "rgba(0, 0, 0, 0.8)",  # Semi-transparente para el blur
                    "backdrop-filter": "blur(10px)",
                    "-webkit-backdrop-filter": "blur(10px)",  # Safari
                    "border-bottom": "1px solid var(--gray-5)",
                    "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.3)",
                    "z-index": "99",
                },
                display=["block", "block", "none"],  # Solo móvil
            ),
        ),
        
        width="100%",
        height="64px",  # Altura fija
        style={
            "position": "sticky",
            "top": "0",
            "z-index": "100",
            "backdrop-filter": "blur(10px)",
            "background": "var(--color-background-alpha)",
            "border-bottom": "1px solid var(--gray-5)",
            "display": "flex",
            "flex-direction": "column",
            "justify-content": "center",
        },
    )
