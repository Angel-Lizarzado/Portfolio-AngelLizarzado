import reflex as rx

def social_link_button(
    platform: str,
    url: str,
    icon: str = None,
) -> rx.Component:
    """
    Botón de enlace social con efectos hover.
    
    Args:
        platform: Nombre de la plataforma (GitHub, LinkedIn, Email)
        url: URL o mailto: del enlace
        icon: Icono opcional (futuro uso)
    
    Returns:
        rx.Component: Botón con enlace social
    """
    return rx.link(
        rx.button(
            platform,
            variant="soft",
            size="3",
            style={
                "transition": "all 0.3s ease",
                "cursor": "pointer",
            },
            _hover={
                "transform": "translateY(-3px)",
                "box_shadow": "0 6px 12px rgba(0, 0, 0, 0.15)",
            },
        ),
        href=url,
        is_external=True,
    )


def social_links(
    github: str = None,
    linkedin: str = None,
    email: str = None,
    twitter: str = None,
    repo_url: str = None,
    layout: str = "horizontal",
) -> rx.Component:
    """
    Componente de enlaces a redes sociales.
    
    Args:
        github: URL de GitHub
        linkedin: URL de LinkedIn
        email: Email (se convertirá en mailto:)
        twitter: URL de Twitter/X
        layout: "horizontal" o "vertical"
    
    Returns:
        rx.Component: Grupo de enlaces sociales
    """
    links = []
    
    if github:
        links.append(social_link_button("GitHub", github))
    
    if linkedin:
        links.append(social_link_button("LinkedIn", linkedin))
    
    if email:
        email_url = f"mailto:{email}" if not email.startswith("mailto:") else email
        links.append(social_link_button("Email", email_url))
    
    if twitter:
        links.append(social_link_button("Twitter", twitter))
        
    if repo_url:
        links.append(social_link_button("Source Code", repo_url))
    
    if not links:
        return rx.box()  # Retornar box vacío si no hay links
    
    if layout == "vertical":
        return rx.vstack(
            *links,
            spacing="3",
            align_items="center",
        )
    else:  # horizontal
        return rx.flex(
            *links,
            spacing="4",
            wrap="wrap",
            justify="center",
        )
