import allure
import pytest
from playwright.sync_api import Page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Проверяем, что это этап вызова (call), а не настройки (setup)
    if report.when == 'call' and report.failed:
        # Достаем страницу из фикстур теста
        page: Page = item.funcargs.get('page')
        if page:
            # 1. Прикрепляем скриншот
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            # 2. Прикрепляем текущий URL (чтобы понимать, где упали)
            allure.attach(
                page.url,
                name="failure_url",
                attachment_type=allure.attachment_type.TEXT
            )