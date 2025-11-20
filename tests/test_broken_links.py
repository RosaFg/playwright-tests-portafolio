"""Tests para detectar enlaces rotos"""
from playwright.sync_api import Page
import re


def test_no_broken_internal_links(page: Page):
    """Verificar que no hay enlaces internos rotos"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    internal_links = page.locator("a[href^='#'], a[href^='/']")
    count = internal_links.count()
    
    broken_links = []
    
    for i in range(min(count, 10)):  
        link = internal_links.nth(i)
        href = link.get_attribute("href")
        
        if href and href.startswith("#"):
            target_id = href[1:]
            target = page.locator(f"#{target_id}, [name='{target_id}']")
            if target.count() == 0:
                broken_links.append(f"Ancla no encontrada: {href}")
    
    assert len(broken_links) == 0, f"Enlaces rotos encontrados:\n" + "\n".join(broken_links)


def test_external_links_have_security(page: Page):
    """Verificar que enlaces externos tienen rel='noopener noreferrer' por seguridad"""
    page.goto("https://portafolio-rosafg.netlify.app/")
    
    external_links = page.locator("a[target='_blank']")
    count = external_links.count()
    
    insecure_links = []
    
    for i in range(count):
        link = external_links.nth(i)
        rel = link.get_attribute("rel") or ""
        href = link.get_attribute("href") or ""
        
        if "noopener" not in rel or "noreferrer" not in rel:
            insecure_links.append(f"Link sin seguridad: {href}")
    
    assert len(insecure_links) == 0, f"Enlaces externos sin protección:\n" + "\n".join(insecure_links)

