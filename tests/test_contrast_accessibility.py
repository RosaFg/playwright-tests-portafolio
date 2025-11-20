"""Tests de contraste y accesibilidad visual"""
from playwright.sync_api import Page


def test_heading_hierarchy(page: Page):
    """Verificar jerarquía correcta de headings (h1, h2, h3...)"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    h1_count = page.locator("h1").count()
    
    assert h1_count == 1, f"Debe haber exactamente un H1 (encontrados: {h1_count})"
    
    h2_count = page.locator("h2").count()
    if h2_count == 0:
        print("\n⚠️  No se encontraron H2, considera usar jerarquía de headings")


def test_links_have_descriptive_text(page: Page):
    """Verificar que los enlaces tienen texto descriptivo"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    links = page.locator("a")
    bad_links = []
    
    for i in range(min(links.count(), 10)):
        link = links.nth(i)
        text = link.inner_text().strip()
        
        if text.lower() in ["click aquí", "aquí", "leer más", "ver más", "click here", "here"]:
            href = link.get_attribute("href")
            bad_links.append(f"Texto poco descriptivo: '{text}' -> {href}")
    
    if bad_links:
        print(f"\n Enlaces con texto poco descriptivo:\n" + "\n".join(bad_links))