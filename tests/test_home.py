import re
from playwright.sync_api import Page, expect


def test_home_title(page: Page):
    """Verificar que el título de la página es correcto"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    expect(page).to_have_title(re.compile("Portafolio|Rosa", re.IGNORECASE))


def test_page_loads_successfully(page: Page):
    """Verificar que la página carga sin errores"""
    response = page.goto("https://portafolio-rosafg.netlify.app/")
    assert response.status == 200, f"La página retornó status {response.status}"