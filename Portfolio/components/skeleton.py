"""Skeleton components for loading states"""

import reflex as rx


def skeleton_card(height: str = "150px") -> rx.Component:
    """Skeleton placeholder for cards"""
    return rx.box(
        rx.skeleton(height=height, width="100%"),
        padding="4",
        border_radius="12px",
        style={
            "background": "var(--gray-2)",
            "border": "1px solid var(--gray-5)",
        },
    )


def skeleton_badge() -> rx.Component:
    """Skeleton placeholder for skill badges"""
    return rx.skeleton(
        height="28px",
        width="80px",
        border_radius="full",
    )


def skeleton_text(width: str = "100%") -> rx.Component:
    """Skeleton placeholder for text"""
    return rx.skeleton(
        height="16px",
        width=width,
        border_radius="md",
    )


def skeleton_heading(width: str = "200px") -> rx.Component:
    """Skeleton placeholder for headings"""
    return rx.skeleton(
        height="32px",
        width=width,
        border_radius="md",
    )


def skeleton_project_card() -> rx.Component:
    """Skeleton for project card"""
    return rx.box(
        rx.vstack(
            rx.skeleton(height="200px", width="100%", border_radius="md"),
            skeleton_heading("180px"),
            skeleton_text("100%"),
            skeleton_text("80%"),
            rx.hstack(
                skeleton_badge(),
                skeleton_badge(),
                skeleton_badge(),
                spacing="2",
            ),
            spacing="3",
            align_items="start",
        ),
        padding="4",
        border_radius="12px",
        style={
            "background": "var(--gray-2)",
            "border": "1px solid var(--gray-5)",
        },
    )


def skeleton_experience_card() -> rx.Component:
    """Skeleton for experience/education card"""
    return rx.box(
        rx.hstack(
            rx.skeleton(height="96px", width="96px", border_radius="md"),
            rx.vstack(
                skeleton_text("150px"),
                skeleton_heading("200px"),
                skeleton_text("100px"),
                spacing="2",
                align_items="start",
            ),
            spacing="4",
        ),
        padding="4",
        border_radius="12px",
        style={
            "background": "var(--gray-2)",
            "border": "1px solid var(--gray-5)",
        },
    )


def skeleton_skills_section() -> rx.Component:
    """Skeleton for entire skills section"""
    return rx.vstack(
        skeleton_heading("300px"),
        rx.vstack(
            skeleton_heading("150px"),
            rx.flex(
                *[skeleton_badge() for _ in range(7)],
                spacing="3",
                wrap="wrap",
            ),
            spacing="2",
        ),
        rx.vstack(
            skeleton_heading("150px"),
            rx.flex(
                *[skeleton_badge() for _ in range(8)],
                spacing="3",
                wrap="wrap",
            ),
            spacing="2",
        ),
        spacing="7",
        width="100%",
    )


def skeleton_projects_section() -> rx.Component:
    """Skeleton for projects section"""
    return rx.vstack(
        skeleton_heading("300px"),
        rx.grid(
            *[skeleton_project_card() for _ in range(3)],
            columns=rx.breakpoints(initial="1", sm="1", md="2", lg="3"),
            spacing="6",
            width="100%",
        ),
        spacing="6",
        width="100%",
    )


def skeleton_experience_section() -> rx.Component:
    """Skeleton for experience section"""
    return rx.vstack(
        rx.center(
            skeleton_heading("300px"),
            width="100%",
            margin_bottom="6",
        ),
        
        rx.grid(
            # Columna izquierda - Educación
            rx.vstack(
                skeleton_heading("150px"),
                *[skeleton_experience_card() for _ in range(2)],
                spacing="4",
                align_items="start",
                width="100%",
            ),
            
            # Columna derecha - Experiencia
            rx.vstack(
                skeleton_heading("200px"),
                rx.vstack(
                    *[skeleton_text("100%") for _ in range(4)],
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
                spacing="4",
                align_items="start",
                width="100%",
            ),
            
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="8",
            width="100%",
        ),
        
        spacing="3",
        align_items="center",
        width="100%",
    )
