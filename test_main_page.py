from playwright.sync_api import sync_playwright


def test_main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://dantist8.ru/", wait_until="domcontentloaded")

        print("Сайт открылся:", page.title())

        # небольшая пауза, чтобы не закрывалось мгновенно
        page.wait_for_timeout(3000)

        assert page.locator("body").is_visible()

        browser.close()


if __name__ == "__main__":
    test_main_page()