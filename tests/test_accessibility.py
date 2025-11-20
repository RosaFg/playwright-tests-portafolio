from playwright.sync_api import Page


def test_images_have_alt(page: Page):
    """Verificar que todas las imágenes tienen atributo alt"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    images = page.locator("img")
    count = images.count()
    
    missing_alt = []
    for i in range(count):
        alt = images.nth(i).get_attribute("alt")
        if alt is None or alt == "":
            src = images.nth(i).get_attribute("src") or "sin src"
            missing_alt.append(f"Imagen {i+1}: {src}")
    
    assert len(missing_alt) == 0, f"Imágenes sin ALT:\n" + "\n".join(missing_alt)


def test_page_has_lang_attribute(page: Page):
    """Verificar que la página tiene el atributo lang definido"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    html = page.locator("html")
    lang = html.get_attribute("lang")
    
    assert lang is not None, "El elemento <html> debe tener atributo 'lang'"
    assert lang != "", "El atributo 'lang' no puede estar vacío"