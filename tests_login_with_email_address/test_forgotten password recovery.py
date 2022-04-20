import pytest
from assertpy import assert_that
from playwright.sync_api import expect


def test_recovery_unregister_user(page):
    test_email = 'adfdsfasdf@wp.pl'
    success_message = page.locator("[data-test=\"text-success-message\"]")

    page.goto("https://login.pracuj.pl/")

    page.locator("text=Zapomniałeś hasła?").click()
    page.locator("[data-test=\"input-forgot-password-email\"]").click()
    page.locator("[data-test=\"input-forgot-password-email\"]").fill(test_email)
    page.locator("[data-test=\"button-forgot-password\"]").click()

    expect(success_message).not_to_contain_text(r"Wysłaliśmy Ci wiadomość na adres" + test_email + "z linkiem do zmiany hasła.")


def test_recovery_register_user(page):
    test_email = 'bond47647@gmail.com'
    success_message = page.locator("[data-test=\"text-success-message\"]")

    page.goto("https://login.pracuj.pl/")

    page.locator("text=Zapomniałeś hasła?").click()
    page.locator("[data-test=\"input-forgot-password-email\"]").click()
    page.locator("[data-test=\"input-forgot-password-email\"]").fill(test_email)
    page.locator("[data-test=\"button-forgot-password\"]").click()

    expect(success_message).to_contain_text(r"Wysłaliśmy Ci wiadomość na adres" + test_email + "z linkiem do zmiany hasła.")


