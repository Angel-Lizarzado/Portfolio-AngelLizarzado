"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Portfolio.sections.hero import hero_section
from Portfolio.sections.about import about_section
from Portfolio.sections.skills import skills_section
from Portfolio.sections.experience import experience_section
from Portfolio.sections.projects import projects_section
from Portfolio.sections.contact import contact_section

from Portfolio.components.navbar import navbar, NavbarState
from Portfolio.utils import get_personal_data

from rxconfig import config


def get_meta_tags() -> list:

    data = get_personal_data()
    #Actualizar con el dominio real al terminar
    base_url = "https://mitsukai.is-a.dev" 
    
    # Reflex usa diccionarios simples para meta tags
    return [
        {"name": "description", "content": f"{data['nombre']} - {data['titulo']}. {data['descripcion']}"},
        {"name": "keywords", "content": "fullstack developer, portfolio, python, javascript, react, reflex, desarrollo web, aws, next.js, node.js, sql, nosql"},
        {"name": "author", "content": data['nombre']},
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
        
        # Open Graph
        {"property": "og:title", "content": f"{data['nombre']} - Portfolio"},
        {"property": "og:description", "content": f"{data['titulo']}. {data['descripcion']}"},
        {"property": "og:type", "content": "website"},
        {"property": "og:url", "content": base_url},
        {"property": "og:image", "content": f"{base_url}/assets/portfolio.png"},
        {"property": "og:locale", "content": "es_ES"},
        
        # Twitter Card
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": f"{data['nombre']} - Portfolio"},
        {"name": "twitter:description", "content": f"{data['titulo']}. {data['descripcion']}"},
        {"name": "twitter:image", "content": f"{base_url}/assets/portfolio.png"},
        
        # Robots
        {"name": "robots", "content": "index, follow"},
    ]


from Portfolio.state import State


def index() -> rx.Component:
    """Página principal del Portfolio"""
    return rx.fragment(
        # Scripts de inicialización
        rx.script(
            """
            // Smooth scroll
            document.documentElement.style.scrollBehavior = 'smooth';
            
            // Cargar tema guardado
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark') {
                document.documentElement.classList.add('dark');
            } else if (savedTheme === 'light') {
                document.documentElement.classList.remove('dark');
            }
            
            // Cargar idioma guardado
            const savedLang = localStorage.getItem('language') || 'es';
            document.documentElement.setAttribute('data-lang', savedLang);
            """
        ),
        
        rx.box(
            # Navbar sticky
            navbar(),
            
            # Contenido principal
            rx.container(
                # Secciones del portfolio
                rx.vstack(
                    rx.box(id="inicio"),  # Anchor para navegación
                    hero_section(),
                    
                    rx.box(id="sobre-mi"),
                    about_section(),
                    
                    rx.box(id="skills"),
                    skills_section(),
                    
                    rx.box(id="experiencia"),
                    experience_section(),
                    
                    rx.box(id="proyectos"),
                    projects_section(),
                    
                    spacing="9",
                    width="100%",
                ),
                
                # Configuración del container
                max_width="1200px",
                padding_x="4",  # Márgenes laterales en móvil
                padding_y="8",
                padding_top="12",  # Más espacio arriba
            ),
            
            # Espaciador antes del footer
            rx.box(height="80px"),
            
            # Footer/Contacto full-width
            rx.box(id="contacto"),
            contact_section(),
            
            width="100%",
            style={
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
            },
        ),
        on_mount=State.on_load,
    )


app = rx.App(
    stylesheets=[
        "styles.css",  # Carga estilos globales desde assets/styles.css
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap",
    ],
    style={
        "font_family": "Inter, sans-serif",
    },
    head_components=[
        rx.el.link(rel="apple-touch-icon", sizes="180x180", href="/apple-touch-icon.png"),
        rx.el.link(rel="icon", type="image/png", sizes="32x32", href="/favicon-32x32.png"),
        rx.el.link(rel="icon", type="image/png", sizes="16x16", href="/favicon-16x16.png"),
        rx.el.link(rel="manifest", href="/site.webmanifest"),
    ],
)
app.add_page(
    index,
    title=f"{get_personal_data()['nombre']} - Portfolio",
    description=f"{get_personal_data()['titulo']}. Portfolio profesional.",
    meta=get_meta_tags(),
)
