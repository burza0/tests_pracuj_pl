import pytest
from playwright.sync_api import expect


def test_blank_password_and_user(page):
    # Go to https://login.pracuj.pl/
    page.goto("https://login.pracuj.pl/")
    # Click [data-test="button-login"]
    page.locator("[data-test=\"button-login\"]").click()

    email = page.locator("[data-test=\"input-email\"]")
    expect(email).to_contain_text(" ")
    assert page.inner_text(
        "._1Y5MF > div:nth-of-type(1) ._1q5DA") == r"Wypełnij to pole.", f"Actual value: {page.inner_text('._1Y5MF > div:nth-of-type(1) ._1q5DA')}"

    password = page.locator("[data-test=\"input-password\"]")
    expect(password).to_contain_text(" ")
    assert page.inner_text(
        "._1Y5MF > div:nth-of-type(2) ._1q5DA") == r"Wypełnij to pole.", f"Actual value: {page.inner_text('._1Y5MF > div:nth-of-type(2) ._1q5DA')}"


def test_unregistered_user_login(page):
    # Go to https://login.pracuj.pl/
    page.goto("https://login.pracuj.pl/")
    # Click [data-test="input-email"]
    page.locator("[data-test=\"input-email\"]").click()
    # Fill [data-test="input-email"]
    page.locator("[data-test=\"input-email\"]").fill("myszkamiki1234567890@gmail.com")
    # Click [data-test="input-password"]
    page.locator("[data-test=\"input-password\"]").click()
    # Fill [data-test="input-password"]
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")
    # Click [data-test="button-login"]
    page.locator("[data-test=\"button-login\"]").click()

    assert page.inner_text("._2jrjW") == r"Możliwe, że nie potwierdziłeś swojego konta lub 3 razy użyłeś złego hasła. Sprawdź pocztę lub spróbuj później."


def test_wrong_username(page):
    # Go to https://login.pracuj.pl/
    page.goto("https://login.pracuj.pl/")

    # Click [data-test="input-email"]
    page.locator("[data-test=\"input-email\"]").click()
    # Fill [data-test="input-email"]
    page.locator("[data-test=\"input-email\"]").fill("dgfdgdfgdfgdf")
    # Click [data-test="input-password"]
    page.locator("[data-test=\"input-password\"]").click()
    # Fill [data-test="input-password"]
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")
    # Click [data-test="button-login"]
    page.locator("[data-test=\"button-login\"]").click()

    locator = page.locator("._3HFOg > ._1q5DA")
    expect(locator).to_be_visible()


