import pytest
from assertpy import assert_that, soft_assertions
from playwright.sync_api import expect


def test_blank_password_and_user(page):
    page.goto("https://login.pracuj.pl/")
    assert page.inner_text("[data-test=\"input-email\"]") == r''
    assert page.inner_text("[data-test=\"input-password\"]") == r''
    page.locator("[data-test=\"button-login\"]").click()

    with soft_assertions():
        validation_email_errors_loc = page.locator(
            "text=Adres e-mailWypełnij to pole. >> [data-test=\"validation-summary-errors\"]")
        assert_that(validation_email_errors_loc.is_visible()).described_as(
            "Email validation-summary-errors is not visible").is_true()

        validation_pass_errors_loc = page.locator(
            "text=visibility_offHasłoWypełnij to pole. >> [data-test=\"validation-summary-errors\"]")
        assert_that(validation_pass_errors_loc.is_visible()).described_as(
            "Password validation-summary-errors is not visible").is_true()


def test_unregistered_user_login(page):
    page.goto("https://login.pracuj.pl/")
    page.locator("[data-test=\"input-email\"]").click()
    page.locator("[data-test=\"input-email\"]").fill("myszkamiki1234567890@gmail.com")
    page.locator("[data-test=\"input-password\"]").click()
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")
    page.locator("[data-test=\"button-login\"]").click()

    text_feedback_loc = page.locator("[data-test=\"text-feedback-message\"]")
    expect(text_feedback_loc).to_be_visible()


def test_wrong_username(page):
    page.goto("https://login.pracuj.pl/")
    page.locator("[data-test=\"input-email\"]").click()
    page.locator("[data-test=\"input-email\"]").fill("dgfdgdfgdfgdf")
    page.locator("[data-test=\"input-password\"]").click()
    page.locator("[data-test=\"input-password\"]").fill("qwertyuiop")
    page.locator("[data-test=\"button-login\"]").click()

    validation_summary_loc = page.locator(
        "//div[.='Uwzględnij znak „@” w adresie e-mail. W adresie „dgfdgdfgdfgdf” brakuje znaku „@”.']")
    expect(validation_summary_loc).to_be_visible()
