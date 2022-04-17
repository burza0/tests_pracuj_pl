import pytest
from assertpy import assert_that, soft_assertions


def test_visibility(page):
    with soft_assertions():

        # page.goto("https://login.pracuj.pl/")

        locators = page.locator("[data-test=\"input-email\"]")
        locators2 = page.locator("[data-test=\"input-password\"]")
        locators3 = page.locator("[data-test=\"button-login\"]")
        locators4 = page.locator("[data-test=\"button-login-facebook\"]")
        locators5 = page.locator("text= Nie masz konta? Zarejestruj się")
        locators6 = page.locator("text=Jesteś pracodawcą? Zaloguj się do Pracuj.pl dla Firm launch")

        if page.locator("[data-test=\"input-email\"]").is_visible():
            assert_that(locators).is_true()
        else:
            assert_that(locators).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("[data-test=\"input-password\"]").is_visible():
            assert_that(locators2).is_true()
        else:
            assert_that(locators2).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("[data-test=\"button-login\"]").is_visible():
            assert_that(locators3).is_true()
        else:
            assert_that(locators3).described_as('!!!!!!!!!!!!!!!No button required!!!!!!!!!!!!!!!').is_true()

        if page.locator("[data-test=\"button-login-facebook\"]").is_visible():
            assert_that(locators4).is_true()
        else:
            assert_that(locators4).described_as('!!!!!!!!!!!!!!!No button required!!!!!!!!!!!!!!!').is_true()

        if page.locator("text= Nie masz konta? Zarejestruj się").is_visible():
            assert_that(locators5).is_true()
        else:
            assert_that(locators5).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("text=Jesteś pracodawcą? Zaloguj się do Pracuj.pl dla Firm launch").is_visible():
            assert_that(locators6).is_true()
        else:
            assert_that(locators6).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()
