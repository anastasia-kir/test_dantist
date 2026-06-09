from playwright.sync_api import sync_playwright


def test_main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://dantist8.ru/", wait_until="domcontentloaded")

        print("Сайт открылся:", page.title())

        assert page.locator("body").is_visible()

        browser.close()