import pytest
from assertpy import assert_that, soft_assertions


def test_visibility(page):
    page.goto("https://login.pracuj.pl/")

    with soft_assertions():
        email_input_loc = page.locator("[data-test=\"input-email\"]")
        assert_that(email_input_loc.is_visible()).described_as("E-mail input is not visible").is_true()

        pass_input_loc = page.locator("[data-test=\"input-password\"]")
        assert_that(pass_input_loc.is_visible()).described_as("Password input is not visible").is_true()

        button_log_loc = page.locator("[data-test=\"button-login\"]")
        assert_that(button_log_loc.is_visible()).described_as("Button-login is not visible").is_true()

        button_face_loc = page.locator("[data-test=\"button-login-facebook\"]")
        assert_that(button_face_loc.is_visible()).described_as("Button-login-facebook is not visible").is_true()

        register_link_loc = page.locator("text= Nie masz konta? Zarejestruj się")
        assert_that(register_link_loc.is_visible()).described_as("Link 'Zarejestruj się' is not visible").is_true()

        login_for_business_loc = page.locator("text=Jesteś pracodawcą? Zaloguj się do Pracuj.pl dla Firm launch")
        assert_that(login_for_business_loc.is_visible()).described_as("Link 'Pracuj.pl dla Firm' is not visible").is_true()


