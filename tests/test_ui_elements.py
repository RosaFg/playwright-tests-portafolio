import re
from playwright.sync_api import Page, expect


def test_about_section_visible(page: Page):
    """Verificar que la sección 'Sobre Mí' es visible"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    section = page.get_by_role("heading", name=re.compile("Sobre Mí|About", re.IGNORECASE))
    expect(section).to_be_visible()


def test_main_heading_exists(page: Page):
    """Verificar que existe un heading principal"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    heading = page.get_by_role("heading").first
    expect(heading).to_be_visible()
