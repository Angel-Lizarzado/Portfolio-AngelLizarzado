# Sistema de Gestión de Datos con JSON

El portfolio ahora utiliza archivos JSON para gestionar toda la información estática. Esto facilita la actualización del contenido sin tocar el código.

## 📁 Estructura de Archivos JSON

### `data/personal.json`
Información personal y general del portfolio:
- Nombre, título, descripción
- Iniciales para el avatar
- Tecnologías principales del hero
- Textos "Sobre Mí"
- Redes sociales (GitHub, LinkedIn, Email, Twitter)
- Copyright del footer

### `data/skills.json`
Habilidades técnicas organizadas por categorías:
- Cada categoría tiene nombre y lista de tecnologías
- Fácil de agregar/quitar skills o categorías

### `data/projects.json`
Proyectos destacados:
- Título, descripción
- Tecnologías usadas
- URLs de GitHub y demo
- URL de imagen o gradiente de fondo

### `data/experience.json`
Educación y experiencia profesional:
- Educación: institución, programa, periodo, logo
- Experiencia: lista de logros/responsabilidades

## 🔧 Cómo Usar

### Actualizar Proyectos

Edita `data/projects.json`:

```json
{
  "proyectos": [
    {
      "titulo": "Mi Nuevo Proyecto",
      "descripcion": "Descripción del proyecto...",
      "tecnologias": ["React", "Node.js"],
      "github_url": "https://github.com/usuario/proyecto",
      "demo_url": "https://mi-proyecto.com",
      "imagen_url": null,
      "bg_color": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    }
  ]
}
```

### Actualizar Skills

Edita `data/skills.json`:

```json
{
  "categorias": [
    {
      "nombre": "Nueva Categoría",
      "tecnologias": ["Tech1", "Tech2", "Tech3"]
    }
  ]
}
```

### Actualizar Información Personal

Edita `data/personal.json`:

```json
{
  "nombre": "Tu Nombre",
  "titulo": "Tu Título",
  "redes_sociales": {
    "github": "https://github.com/tu-usuario",
    "linkedin": "https://linkedin.com/in/tu-perfil",
    "email": "tu@email.com"
  }
}
```

## 📝 Secciones Ya Migradas

- ✅ **Projects** - Usa `data/projects.json`
- ✅ **Skills** - Usa `data/skills.json`
- ⏳ **Hero** - Todavía con datos hardcoded
- ⏳ **About** - Todavía con datos hardcoded
- ⏳ **Experience** - Todavía con datos hardcode
- ⏳ **Contact** - Todavía con datos hardcoded

Las secciones restantes se pueden migrar siguiendo el mismo patrón.

## 🎯 Beneficios

1. **Fácil mantenimiento** - Solo editas JSONs, no código Python
2. **Separación de contenido** - El código se enfoca en la presentación
3. **Reutilizable** - El mismo código funciona con diferentes datos
4. **Escalable** - Fácil agregar más proyectos, skills, etc.
5. **Sin recompilar** - Cambios en JSON solo requieren reiniciar servidor
