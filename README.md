# Portfolio Profesional - Angel Lizarzado

Este repositorio contiene el código fuente de mi portfolio personal, desarrollado como una Single Page Application (SPA) moderna, rápida y escalable utilizando **Python** y **Reflex**.

El proyecto destaca por su arquitectura limpia, automatización de procesos (traducción y despliegue) y un diseño UI/UX cuidado al detalle.

🔗 **Demo en vivo:** [https://portfolio-aqua-panda.reflex.run](https://portfolio-aqua-panda.reflex.run)

## 🛠️ Stack Tecnológico

*   **Framework Principal:** [Reflex](https://reflex.dev/) (Python puro para Frontend y Backend).
*   **Lenguaje:** Python 3.12+.
*   **Estilos:** CSS3 nativo + Reflex Styling (Flexbox/Grid).
*   **Internacionalización:** Sistema propio basado en JSON + Google Translate API.
*   **Despliegue:** Reflex Cloud.

## ✨ Características Clave

*   **Diseño Responsive:** Adaptable a móviles, tablets y escritorio.
*   **Modo Oscuro/Claro:** Persistencia de tema basada en preferencias del usuario.
*   **Bilingüe (ES/EN):** Sistema de traducción instantánea con detección automática.
*   **Arquitectura de Datos:** Todo el contenido (experiencia, proyectos, skills) se gestiona desde archivos JSON en `/data`, separando la lógica del contenido.
*   **Animaciones:** Transiciones suaves y micro-interacciones.

## 🤖 Automatización y Flujo de Trabajo

Este proyecto implementa un flujo de trabajo CI/CD simplificado mediante **Git Hooks**, eliminando tareas repetitivas:

### 1. Traducción Automática (`pre-commit`)
No es necesario escribir los textos en inglés manualmente.
*   **Cómo funciona:** Al hacer un commit, un script detecta cambios en los archivos JSON en español.
*   **Acción:** Genera automáticamente la versión en inglés usando `deep-translator` y actualiza el JSON antes de confirmar el commit.

### 2. Despliegue Automático (`pre-push`)
Garantiza que lo que está en GitHub es lo que está en producción.
*   **Cómo funciona:** Al hacer `git push`.
*   **Acción:** Ejecuta `reflex deploy`. Si el despliegue falla, el push se cancela para evitar subir código roto.

## 🚀 Instalación y Desarrollo Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Angel-Lizarzado/Portfolio-AngelLizarzado.git
    cd Portfolio-AngelLizarzado
    ```

2.  **Crear entorno virtual e instalar dependencias:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Ejecutar en modo desarrollo:**
    ```bash
    reflex run
    ```
    La aplicación estará disponible en `http://localhost:3000`.

## 📂 Estructura del Proyecto

```text
Portfolio/
├── .git/hooks/      # Scripts de automatización (pre-commit, pre-push)
├── assets/          # Imágenes, fuentes y estilos globales
├── data/            # Contenido JSON (projects, experience, skills)
├── Portfolio/       # Código fuente de la aplicación
│   ├── components/  # Componentes reutilizables (navbar, cards, badges)
│   ├── sections/    # Secciones principales de la página
│   ├── utils/       # Scripts de utilidad (translator.py)
│   ├── state.py     # Gestión de estado global (tema, idioma)
│   └── Portfolio.py # Punto de entrada y configuración
└── requirements.txt # Dependencias del proyecto
```

---
Desarrollado con ❤️ por **Angel Lizarzado**.
