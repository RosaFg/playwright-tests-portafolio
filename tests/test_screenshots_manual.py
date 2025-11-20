from playwright.sync_api import Page
from pathlib import Path
from datetime import datetime

SCREENSHOT_DIR = Path("screenshots")


def save_screenshot(page: Page, name: str, full_page: bool = True):
    """
    Función helper para guardar screenshots con timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = SCREENSHOT_DIR / filename
    
    page.screenshot(path=str(filepath), full_page=full_page)
    print(f"\n Screenshot guardado: {filepath}")
    return filepath


def test_home_with_screenshots(page: Page):
    """Capturar screenshots de la página principal"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    save_screenshot(page, "01_home_full_page")
    
    save_screenshot(page, "02_home_viewport", full_page=False)
    
    page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
    save_screenshot(page, "03_home_middle")


def test_contact_form_workflow(page: Page):
    """Capturar el flujo completo del formulario de contacto"""
    page.goto("https://portafolio-rosafg.netlify.app/#contact")
    
    save_screenshot(page, "04_form_empty")
    
    page.get_by_placeholder("Nombre", "Name").fill("Test User")
    save_screenshot(page, "05_form_name_filled")
    
    page.get_by_placeholder("Correo", "Email").fill("test@example.com")
    save_screenshot(page, "06_form_email_filled")
    
    page.get_by_placeholder("Mensaje", "Message").fill("Este es un mensaje de prueba")
    save_screenshot(page, "07_form_complete")


def test_responsive_screenshots(page: Page):
    """Capturar screenshots en diferentes dispositivos"""
    url = "https://portafolio-rosafg.netlify.app/"
    
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto(url)
    save_screenshot(page, "08_mobile_375x812")
    
    page.set_viewport_size({"width": 768, "height": 1024})
    page.goto(url)
    save_screenshot(page, "09_tablet_768x1024")
    
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(url)
    save_screenshot(page, "10_desktop_1920x1080")


def test_screenshot_specific_element(page: Page):
    """Capturar screenshot de un elemento específico"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    header = page.locator("header, nav").first
    if header.count() > 0:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = SCREENSHOT_DIR / f"11_header_only_{timestamp}.png"
        header.screenshot(path=str(filepath))
        print(f"\n📸 Screenshot del header: {filepath}")


def test_dark_mode_comparison(page: Page):
    """Capturar screenshots con diferentes temas (si aplica)"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    save_screenshot(page, "12_light_mode")
    
    dark_mode_button = page.locator("button[aria-label*='dark'], button[aria-label*='theme']")
    if dark_mode_button.count() > 0:
        dark_mode_button.click()
        page.wait_for_timeout(500)
        save_screenshot(page, "13_dark_mode")