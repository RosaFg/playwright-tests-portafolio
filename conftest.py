import pytest
from pathlib import Path
from datetime import datetime
from playwright.sync_api import Page


SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page: Page):
    """
    Fixture que captura screenshot automáticamente cuando un test falla
    """
    yield
    
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{test_name}_{timestamp}_FAILED.png"
        screenshot_path = SCREENSHOT_DIR / screenshot_name
        
        try:
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"\nScreenshot guardado: {screenshot_path}")
        except Exception as e:
            print(f"\nError al capturar screenshot: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que captura el resultado de cada fase del test
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture
def save_screenshot():
    """
    Fixture opcional para guardar screenshots manualmente
    """
    def _save_screenshot(page: Page, name: str, full_page: bool = True):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = SCREENSHOT_DIR / filename
        
        page.screenshot(path=str(filepath), full_page=full_page)
        print(f"\nScreenshot guardado: {filepath}")
        return filepath
    
    return _save_screenshot