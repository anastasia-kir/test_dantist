from playwright.sync_api import sync_playwright


def test_menu():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://dantist8.ru/", wait_until="domcontentloaded")

        # ожидаем загрузку страницы
        page.wait_for_timeout(2000)

        assert (
            page.locator("text=Услуги").count() > 0 or
            page.locator("text=Врачи").count() > 0 or
            page.locator("text=Контакты").count() > 0
        )

        browser.close()
