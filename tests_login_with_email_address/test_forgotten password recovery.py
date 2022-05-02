import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize(
    'input_email', (pytest.param('bond47647gmail.com', id='bond47647gmail.com  - invalid address'),
                    pytest.param('bond47647@gmail.com', id='bond47647@gmail.com  - valid address'),
                    pytest.param('dsfdsfsdfs@wp.pl', id='dsfdsfsdfs@wp.pl - unregistered user')))
def test_password_recovery(page, input_email):
    page.goto("https://login.pracuj.pl/")

    page.locator("text=Zapomniałeś hasła?").click()
    page.locator("[data-test=\"input-forgot-password-email\"]").click()
    page.locator("[data-test=\"input-forgot-password-email\"]").fill(input_email)
    page.locator("[data-test=\"button-forgot-password\"]").click()
    success_message = page.locator("[data-test=\"text-success-message\"]")
    expect(success_message).to_contain_text(
        r"Wysłaliśmy Ci wiadomość na adres" + input_email + "z linkiem do zmiany hasła.")
