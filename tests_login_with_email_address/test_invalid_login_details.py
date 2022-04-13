import pytest
from playwright.sync_api import expect


def test_blank_password_and_user(page):
    page.goto("https://login.pracuj.pl/")
    page.locator("[data-test=\"button-login\"]").click()
    email = page.locator("[data-test=\"input-email\"]")
    expect(email).to_contain_text(" ")
    assert page.locator("text=Adres e-mailWypełnij to pole. >> [data-test=\"validation-summary-errors\"]").is_visible()

    password = page.locator("[data-test=\"input-password\"]")
    expect(password).to_contain_text(" ")
    assert page.locator(
        "text=visibility_offHasłoWypełnij to pole. >> [data-test=\"validation-summary-errors\"]").is_visible()


def test_unregistered_user_login(page):
    page.goto("https://login.pracuj.pl/")
    page.locator("[data-test=\"input-email\"]").click()
    page.locator("[data-test=\"input-email\"]").fill("myszkamiki1234567890@gmail.com")
    page.locator("[data-test=\"input-password\"]").click()
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")
    page.locator("[data-test=\"button-login\"]").click()

    locator = page.locator("[data-test=\"text-feedback-message\"]")
    expect(locator).to_be_visible()


def test_wrong_username(page):
    page.goto("https://login.pracuj.pl/")
    page.locator("[data-test=\"input-email\"]").click()
    page.locator("[data-test=\"input-email\"]").fill("dgfdgdfgdfgdf")
    page.locator("[data-test=\"input-password\"]").click()
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")
    page.locator("[data-test=\"button-login\"]").click()

