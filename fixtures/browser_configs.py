# fixtures/browser_settings.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "base_url": base_url # Берем из конфига pytest.ini
    }