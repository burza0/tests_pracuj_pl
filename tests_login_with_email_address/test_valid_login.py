import pytest


def test_valid_login(page):
    page.goto("https://login.pracuj.pl/")
    page.locator("[data-test=\"input-email\"]").click()
    page.locator("[data-test=\"input-email\"]").fill("bond47647@gmail.com")
    page.locator("[data-test=\"input-password\"]").click()
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")

    with page.expect_navigation():
        page.locator("[data-test=\"button-login\"]").click()
    with page.expect_navigation():
        page.locator("[data-test=\"button-accept-all-in-general\"]").click()
    page.locator("[data-test=\"button-accountMenu\"]").click()
    page.locator("[data-test=\"section-desktopLayout\"] [data-test=\"text-userEmail\"]").click()

    assert page.inner_text(
        "[data-test=\"section-desktopLayout\"] [data-test=\"text-userEmail\"]") == r'bond47647@gmail.com'
