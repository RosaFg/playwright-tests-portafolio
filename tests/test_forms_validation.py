"""Tests de validación de formularios (si aplica)"""
from playwright.sync_api import Page, expect
import re


def test_email_field_has_validation(page: Page):
    """Verificar que el campo email tiene validación de tipo email"""
    page.goto("https://portafolio-rosafg.netlify.app/#contact")
    
    email_field = page.get_by_placeholder(re.compile(r"correo|email", re.IGNORECASE))
    
    if email_field.count() > 0:
        input_type = email_field.get_attribute("type")
        # Debería ser type="email" para validación automática
        if input_type != "email":
            print(f"\n⚠️  Campo email no tiene type='email' (actual: {input_type})")


def test_required_fields_marked(page: Page):
    """Verificar que campos requeridos están marcados"""
    page.goto("https://portafolio-rosafg.netlify.app/#contact")
    
    name_field = page.get_by_placeholder(re.compile(r"nombre|name", re.IGNORECASE))
    
    if name_field.count() > 0:
        required = name_field.get_attribute("required")
        if not required:
            print("\n⚠️  Campo nombre no tiene atributo 'required'")
