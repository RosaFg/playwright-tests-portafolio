import re
from playwright.sync_api import Page, expect

devices = {
    "mobile": {"width": 375, "height": 812},
    "tablet": {"width": 768, "height": 1024},
    "desktop": {"width": 1920, "height": 1080},
}


def test_responsive_mobile(page: Page):
    """Verificar diseño responsive en móvil"""
    page.set_viewport_size(devices["mobile"])
    page.goto("https://portafolio-rosafg.netlify.app/")
    expect(page).to_have_title(re.compile("Portafolio|Rosa", re.IGNORECASE))
    
    heading = page.get_by_role("heading").first
    expect(heading).to_be_in_viewport()


def test_responsive_tablet(page: Page):
    """Verificar diseño responsive en tablet"""
    page.set_viewport_size(devices["tablet"])
    page.goto("https://portafolio-rosafg.netlify.app/")
    expect(page).to_have_title(re.compile("Portafolio|Rosa", re.IGNORECASE))


def test_responsive_desktop(page: Page):
    """Verificar diseño responsive en desktop"""
    page.set_viewport_size(devices["desktop"])
    page.goto("https://portafolio-rosafg.netlify.app/")
    expect(page).to_have_title(re.compile("Portafolio|Rosa", re.IGNORECASE))
