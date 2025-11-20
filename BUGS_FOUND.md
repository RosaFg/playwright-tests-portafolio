#  Bugs Encontrados en el Portafolio

Este documento lista los bugs reales encontrados durante las pruebas automatizadas del portafolio.

**Fecha del análisis**: Noviembre 2025  
**URL testeada**: https://portafolio-rosafg.netlify.app/

---

##  Críticos (Seguridad)
### 1. Enlaces externos sin protección de seguridad
**Test que lo detecta**: `test_broken_links.py::test_external_links_have_security`
**Problema**:  
Los enlaces externos con `target="_blank"` no tienen los atributos de seguridad `rel="noopener noreferrer"`, lo que representa una vulnerabilidad de seguridad conocida como "tabnabbing".
**Enlaces afectados**:
- LinkedIn: `https://www.linkedin.com/in/rosafg/`
- GitHub perfil: `https://github.com/RosaFg`
- Email: `mailto:rosafuegos@gmail.com`
- Proyecto Parabank: `https://github.com/RosaFg/parabank-testing-playwright`
- Proyecto PDF Editor: `https://github.com/RosaFg/PDF-Editor`
- Proyecto Word Editor: `https://github.com/RosaFg/word-editor`

**Impacto**: 
- **Seguridad**: Permite que la página vinculada acceda al objeto `window.opener`
- **Performance**: La nueva pestaña se ejecuta en el mismo proceso, afectando el rendimiento

**Solución recomendada**:
```html
<!-- Antes -->
<a href="https://github.com/RosaFg" target="_blank">GitHub</a>

<!-- Después -->
<a href="https://github.com/RosaFg" target="_blank" rel="noopener noreferrer">GitHub</a>
```

**Prioridad**:  Alta

---

##  Advertencias (SEO)
### 2. Falta meta description
**Test que lo detecta**: `test_seo.py::test_has_meta_description`
**Problema**:  
La página no tiene una meta description definida, lo que afecta negativamente el SEO.

**Impacto**:
- Los motores de búsqueda no tienen una descripción para mostrar en resultados
- Reduce el CTR (Click Through Rate) en buscadores
- Afecta el posicionamiento SEO

**Solución recomendada**:
```html
<head>
  <meta name="description" content="Portafolio de Rosa Fuentes - QA Automation Engineer especializada en pruebas automatizadas con Playwright, Selenium y testing de APIs">
</head>
```

**Prioridad**:  Media
---
### 3. Falta favicon
**Test que lo detecta**: `test_seo.py::test_has_favicon`
**Problema**:  
No hay favicon configurado, lo que afecta la identidad visual del sitio.

**Impacto**:
- Las pestañas del navegador muestran un ícono genérico
- Reduce profesionalismo y reconocimiento de marca
- Dificulta identificar la pestaña entre muchas abiertas

**Solución recomendada**:
```html
<head>
  <link rel="icon" type="image/png" href="/favicon.png">
  <link rel="shortcut icon" href="/favicon.ico">
</head>
```

**Prioridad**:  Media

---

##  Elementos funcionando correctamente

Los siguientes aspectos fueron validados y funcionan correctamente:

- **Accesibilidad**: Todas las imágenes tienen atributo `alt`
- **Internacionalización**: La página tiene atributo `lang` definido
- **Responsive**: El diseño se adapta correctamente a móvil, tablet y desktop
- **Performance**: Tiempo de carga menor a 2 segundos
- **Formulario**: Todos los campos del formulario son funcionales
- **Navegación**: Enlaces internos funcionan correctamente
- **Mobile**: Viewport meta tag configurado correctamente
- **Legibilidad**: Tamaño de texto adecuado en móvil (17.6px)
- **Jerarquía**: Estructura correcta de headings (H1, H2, H3)
---
##  Resumen de Tests
| Estado | Cantidad | Porcentaje |
|--------|----------|------------|
|  Pasados | 25 | 86% |
|  Fallidos | 3 | 14% |
| **Total** | **29** | **100%** |

---

##  Recomendaciones de priorización
1. **Inmediato** (esta semana):
   - Agregar `rel="noopener noreferrer"` a todos los enlaces externos

2. **Corto plazo** (próximo sprint):
   - Agregar meta description
   - Crear y configurar favicon

3. **Seguimiento continuo**:
   - Ejecutar tests automatizados en cada deploy
   - Monitorear nuevos enlaces externos

---

## Notas técnicas

### Cómo reproducir los tests:

```bash
# Ejecutar todos los tests
pytest -v

# Ejecutar solo tests de seguridad
pytest tests/test_broken_links.py -v

# Ejecutar solo tests de SEO
pytest tests/test_seo.py -v

# Generar reporte HTML
pytest --html=report.html --self-contained-html
```

### Herramientas utilizadas:
- **Playwright** 1.40.0
- **Pytest** 8.0.0
- **Firefox** (navegador principal de pruebas)

---
**Documentado por**: Rosa Fuentes
**Última actualización**: Noviembre 2025