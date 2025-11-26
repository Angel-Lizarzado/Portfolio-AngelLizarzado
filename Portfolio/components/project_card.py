import reflex as rx
from Portfolio.components.skill_badge import skill_badge

def project_card(
    title: str,
    description: str,
    technologies: list[str],
    github_url: str = None,
    demo_url: str = None,
    image_url: str = None,
    bg_color: str = None,
) -> rx.Component:
    """
    Componente para cards de proyectos con imagen, descripción y enlaces.
    
    Args:
        title: Título del proyecto
        description: Descripción del proyecto
        technologies: Lista de tecnologías usadas
        github_url: URL del repositorio GitHub (opcional)
        demo_url: URL de la demo/website (opcional)
        image_url: URL de la imagen del proyecto (opcional)
        bg_color: Color de fondo si no hay imagen (opcional)
    
    Returns:
        rx.Component: Card de proyecto con hover effects
    """
    # Contenido superior (imagen o color de fondo)
    top_content = []
    if image_url:
        top_content.append(
            rx.image(
                src=image_url,
                width="100%",
                height="200px",
                object_fit="cover",
                border_radius="8px 8px 0 0",
            )
        )
    elif bg_color:
        top_content.append(
            rx.box(
                width="100%",
                height="120px",
                background=bg_color,
                border_radius="8px 8px 0 0",
            )
        )
    
    # Badges de tecnologías
    tech_badges = rx.flex(
        *[skill_badge(tech, size="1") for tech in technologies],
        spacing="2",
        wrap="wrap",
    )
    
    # Botones de enlaces
    links = []
    if github_url:
        links.append(
            rx.link(
                rx.button(
                    "GitHub",
                    variant="soft",
                    size="2",
                    style={
                        "transition": "all 0.2s ease",
                    },
                ),
                href=github_url,
                is_external=True,
            )
        )
    if demo_url:
        links.append(
            rx.link(
                rx.button(
                    "Demo",
                    variant="solid",
                    size="2",
                    style={
                        "transition": "all 0.2s ease",
                    },
                ),
                href=demo_url,
                is_external=True,
            )
        )
    
    links_section = rx.flex(
        *links,
        spacing="3",
        width="100%",
    ) if links else rx.box()
    
    return rx.card(
        rx.vstack(
            *top_content,
            rx.vstack(
                rx.heading(title, size="5", weight="bold"),
                rx.text(
                    description,
                    size="3",
                    color="gray",
                ),
                tech_badges,
                links_section,
                spacing="3",
                align_items="start",
                padding="4",
            ),
            spacing="0",
            align_items="start",
            width="100%",
        ),
        padding="0",
        style={
            "transition": "all 0.3s ease",
            "overflow": "hidden",
        },
        _hover={
            "transform": "scale(1.02)",
            "box_shadow": "0 12px 24px rgba(0, 0, 0, 0.15)",
            "border_color": "cyan",
        },
    )
