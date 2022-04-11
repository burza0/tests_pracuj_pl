import pytest
from playwright.sync_api import expect


def test_visibility(page):
    # Go to https://login.pracuj.pl/
    page.goto("https://login.pracuj.pl/")
    assert page.is_visible("[data-test=\"input-email\"]")
    assert page.is_visible("[data-test=\"input-password\"]")
    assert page.is_visible("[data-test=\"button-login\"]")
    assert page.is_visible("[data-test=\"button-login-facebook\"]")
    assert page.locator("text=Nie masz konta? Zarejestruj się")
    assert page.locator("text=Jesteś pracodawcą? Zaloguj się do Pracuj.pl dla Firm launch")
    page.locator("text=Zapomniałeś hasła?").click()
    expect(page).to_have_url("https://login.pracuj.pl/przypomnij-haslo")
