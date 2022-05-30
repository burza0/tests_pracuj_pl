# Test design of the "Login with email address" functionality of the pracuj.pl website

> ### Login with email address

1. Checking the visibility of all elements of the login form 

* [display all fields, buttons and links](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_visibility_of_elements.py)

2. Verification of login with valid data 

* [login with a valid username and password](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_valid_login.py)

3. Verification of login with invalid data 

* [login with blank email address and password](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_invalid_login_details.py)
* [unregistered user login](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_invalid_login_details.py) 
* [login with wrong username](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_invalid_login_details.py) 

4. Verification of forgotten password recovery

* [password recovery for a registered user](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_forgotten%20password%20recovery.py) 
* [password recovery for unregistered user](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_forgotten%20password%20recovery.py) 

5. Verification of the correctness of validation messages

* [display message for an email address without a subdomain](#general-information)
* [display message for email address without @](#general-information) 
* [display message for an email with two @](#general-information) 
* [display a message for an empty password field](#general-information) 

6. Verify that the "Pokaż/Ukryj hasło" option is working correctly.

* [showing the hidden password](https://github.com/burza0/tests_pracuj_pl/blob/tests-patch-3/tests_login_with_email_address/test_verify_show_hide_password.py)
