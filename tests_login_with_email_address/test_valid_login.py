import pytest


def test_valid_login(page):
    # Go to https://login.pracuj.pl/
    page.goto("https://login.pracuj.pl/")

    # Click [data-test="input-email"]
    page.locator("[data-test=\"input-email\"]").click()
    # Fill [data-test="input-email"]
    page.locator("[data-test=\"input-email\"]").fill("bond47647@gmail.com")
    # Click [data-test="input-password"]
    page.locator("[data-test=\"input-password\"]").click()
    # Fill [data-test="input-password"]
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")
    # Click [data-test="button-login"]
    # with page.expect_navigation(url="https://www.pracuj.pl/apps/konto/rekomendowane-oferty"):
    with page.expect_navigation():
        page.locator("[data-test=\"button-login\"]").click()
    # Click [data-test="button-accept-all-in-general"]
    with page.expect_navigation():
        page.locator("[data-test=\"button-accept-all-in-general\"]").click()
    # Click [data-test="button-accountMenu"]
    page.locator("[data-test=\"button-accountMenu\"]").click()
    # Click [data-test="section-desktopLayout"] [data-test="text-userEmail"]
    page.locator("[data-test=\"section-desktopLayout\"] [data-test=\"text-userEmail\"]").click()

    assert page.inner_text(
        "[data-test=\"section-desktopLayout\"] [data-test=\"text-userEmail\"]") == r'bond47647@gmail.com'
