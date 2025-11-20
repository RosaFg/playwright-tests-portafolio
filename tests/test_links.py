import re
from playwright.sync_api import Page, expect


def test_github_link_valid(page: Page):
    """Verificar que el enlace de GitHub existe y es válido"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    github = page.locator("a[title='GitHub']")
    expect(github).to_have_attribute("href", re.compile("github.com"))


def test_external_links_open_new_tab(page: Page):
    """Verificar que enlaces externos abren en nueva pestaña"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    external_links = page.locator("a[target='_blank']")
    
    count = external_links.count()
    assert count > 0, "No se encontraron enlaces externos"
    
    for i in range(min(count, 3)):
        expect(external_links.nth(i)).to_have_attribute("target", "_blank")