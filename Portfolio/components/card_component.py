import reflex as rx

def custom_card(
    *children,
    hover_border_color: str = "cyan",
    padding: str = "4",
    width: str = "100%",
    **kwargs
) -> rx.Component:
    """
    Componente de card reutilizable con efectos hover.
    
    Args:
        *children: Componentes hijos a renderizar dentro de la card
        hover_border_color: Color del borde al hacer hover
        padding: Padding interno de la card
        width: Ancho de la card
        **kwargs: Props adicionales para rx.card
    
    Returns:
        rx.Component: Card con transiciones suaves
    """
    return rx.card(
        *children,
        padding=padding,
        width=width,
        style={
            "transition": "all 0.3s ease",
            "cursor": "pointer",
        },
        _hover={
            "border_color": hover_border_color,
            "box_shadow": f"0 8px 16px rgba(0, 0, 0, 0.1)",
        },
        **kwargs
    )
