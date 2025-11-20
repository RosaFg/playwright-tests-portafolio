from playwright.sync_api import Page


def test_has_meta_description(page: Page):
    """Verificar que existe meta description para SEO"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    meta_description = page.locator('meta[name="description"]')
    assert meta_description.count() > 0, "Falta meta description para SEO"
    
    content = meta_description.get_attribute("content")
    assert content and len(content) > 50, f"Meta description muy corta: {len(content) if content else 0} caracteres (mínimo: 50)"


def test_has_meta_keywords(page: Page):
    """Verificar que existen meta keywords (opcional pero recomendado)"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    meta_keywords = page.locator('meta[name="keywords"]')
    if meta_keywords.count() > 0:
        content = meta_keywords.get_attribute("content")
        assert content and len(content) > 10, "Meta keywords muy corto"


def test_has_favicon(page: Page):
    """Verificar que existe un favicon"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    favicon = page.locator('link[rel="icon"], link[rel="shortcut icon"]')
    assert favicon.count() > 0, "Falta el favicon"
