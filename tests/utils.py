from playwright.sync_api import sync_playwright


def open_page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://dantist8.ru/")
    return p, browser, page