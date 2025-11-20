import re
from playwright.sync_api import Page, expect


def test_contact_form_elements(page: Page):
    """Verificar que existen todos los elementos del formulario"""
    page.goto("https://portafolio-rosafg.netlify.app/#contact")
    
    expect(page.get_by_placeholder(re.compile("Nombre|Name", re.IGNORECASE))).to_be_visible()
    expect(page.get_by_placeholder(re.compile("Correo|Email", re.IGNORECASE))).to_be_visible()
    expect(page.get_by_placeholder(re.compile("Mensaje|Message", re.IGNORECASE))).to_be_visible()
    
    submit = page.get_by_role("button", name=re.compile("Enviar|Send", re.IGNORECASE))
    expect(submit).to_be_visible()


def test_fill_contact_form(page: Page):
    """Verificar que se pueden llenar los campos del formulario"""
    page.goto("https://portafolio-rosafg.netlify.app/#contact")
    
    page.get_by_placeholder(re.compile("Nombre|Name", re.IGNORECASE)).fill("Test QA User")
    page.get_by_placeholder(re.compile("Correo|Email", re.IGNORECASE)).fill("test@example.com")
    page.get_by_placeholder(re.compile("Mensaje|Message", re.IGNORECASE)).fill("Mensaje de prueba automatizado")
    
    name_value = page.get_by_placeholder(re.compile("Nombre|Name", re.IGNORECASE)).input_value()
    assert "Test QA" in name_value, "El campo nombre no se llenó correctamente"


def test_submit_button_clickable(page: Page):
    """Verificar que el botón de enviar es clickeable"""
    page.goto("https://portafolio-rosafg.netlify.app/#contact")
    
    submit_button = page.get_by_role("button", name=re.compile("Enviar|Send", re.IGNORECASE))
    expect(submit_button).to_be_enabled()



"""Tests de rendimiento del portafolio"""
from playwright.sync_api import Page


def test_load_time_under_5_seconds(page: Page):
    """Verificar que la página carga en menos de 5 segundos"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    timing = page.evaluate("""
        () => {
            const timing = performance.timing;
            return timing.loadEventEnd - timing.navigationStart;
        }
    """)
    
    assert timing < 5000, f"Página tardó {timing}ms en cargar (máximo: 5000ms)"


def test_no_console_errors(page: Page):
    """Verificar que no hay errores críticos en la consola"""
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    critical_errors = [e for e in errors if "favicon" not in e.lower() and "404" not in e]
    
    assert len(critical_errors) == 0, f"Se encontraron errores: {critical_errors}"
