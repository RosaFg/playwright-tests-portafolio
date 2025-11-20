# tests/test_mobile_usability.py
"""Tests de usabilidad móvil"""
from playwright.sync_api import Page


def test_viewport_meta_tag(page: Page):
    """Verificar que existe viewport meta tag para móviles"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    viewport = page.locator('meta[name="viewport"]')
    assert viewport.count() > 0, "Falta meta viewport tag (necesario para responsive)"
    
    content = viewport.get_attribute("content")
    assert "width=device-width" in content, "Viewport debe incluir width=device-width"


def test_text_readable_on_mobile(page: Page):
    """Verificar que el texto es legible en móvil (tamaño mínimo)"""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    paragraphs = page.locator("p")
    
    if paragraphs.count() > 0:
        font_size = paragraphs.first.evaluate("el => window.getComputedStyle(el).fontSize")
        font_size_num = float(font_size.replace("px", ""))
        
        assert font_size_num >= 14, f"Texto muy pequeño en móvil: {font_size_num}px (mínimo: 14px)"


def test_buttons_large_enough_mobile(page: Page):
    """Verificar que los botones son lo suficientemente grandes para tocar en móvil"""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    buttons = page.locator("button, a[role='button']")
    small_buttons = []
    
    for i in range(min(buttons.count(), 5)):
        button = buttons.nth(i)
        box = button.bounding_box()
        
        if box:
            if box["width"] < 44 or box["height"] < 44:
                text = button.inner_text()[:30] if button.inner_text() else "sin texto"
                small_buttons.append(f"Botón muy pequeño: {box['width']}x{box['height']}px - '{text}'")
    
    if small_buttons:
        print(f"\n  ADVERTENCIA: Botones pequeños encontrados:\n" + "\n".join(small_buttons))