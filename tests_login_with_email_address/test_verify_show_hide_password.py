from playwright.sync_api import expect


def test_show_hide_password(page):
    text_pass = 'gsdfgdfgdf'
    page.goto("https://login.pracuj.pl/")

    page.locator("[data-test=\"input-password\"]").click()
    page.locator("[data-test=\"input-password\"]").fill(text_pass)
    page.locator("text=visibility_off").click()
    expect(page.locator("[data-test=\"input-password\"]")).to_have_value(text_pass)
