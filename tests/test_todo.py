from playwright.sync_api import Page, expect
from config import settings

def test_add_todo(page: Page):
    page.goto(f"{settings.http_client.client_url}todomvc/#/")
    
    new_todo = page.get_by_placeholder("What needs to be done?")
    new_todo.fill("Создать первый сценарий playwright")
    new_todo.press("Enter")
    
    expect(page.get_by_test_id("todo-title")).to_have_text("Создать первый сценарий playwright")