import pytest
from assertpy import assert_that, soft_assertions, soft_fail


def test_visibility(page, locators=None, locators2=None, locators3=None, locators4=None, locators5=None, locators6=None):
    with soft_assertions():

        page.goto("https://login.pracuj.pl/")
        if page.locator("[data-test=\"input-email\"]").is_visible():
            locators = page.locator("[data-test=\"input-email\"]")
            assert_that(locators).is_true()
        else:
            assert_that(locators).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("[data-test=\"input-password\"]").is_visible():
            locators2 = page.locator("[data-test=\"input-password\"]")
            assert_that(locators2).is_true()
        else:
            assert_that(locators2).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("[data-test=\"button-login\"]").is_visible():
            locators3 = page.locator("[data-test=\"button-login\"]")
            assert_that(locators3).is_true()
        else:
            assert_that(locators3).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("[data-test=\"button-login-facebook\"]").is_visible():
            locators4 = page.locator("[data-test=\"button-login-facebook\"]")
            assert_that(locators4).is_true()
        else:
            assert_that(locators4).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("text= Nie masz konta? Zarejestruj się").is_visible():
            locators5 = page.locator("text= Nie masz konta? Zarejestruj się")
            assert_that(locators5).is_true()
        else:
            assert_that(locators5).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()

        if page.locator("text=Jesteś pracodawcą? Zaloguj się do Pracuj.pl dla Firm launch").is_visible():
            locators6 = page.locator("text=Jesteś pracodawcą? Zaloguj się do Pracuj.pl dla Firm launch")
            assert_that(locators6).is_true()
        else:
            assert_that(locators6).described_as('!!!!!!!!!!!!!!!No selector required!!!!!!!!!!!!!!!').is_true()




