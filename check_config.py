from config import settings

print(f"Базовый URL: {settings.http_client.url}")
print(f"Путь к Allure: {settings.allure_results_dir}")