from playwright.sync_api import sync_playwright


def test_forms():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://dantist8.ru/", wait_until="domcontentloaded")

        assert page.locator("input").count() > 0
        assert page.locator("button").count() > 0

        browser.close()