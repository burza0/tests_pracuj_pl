# Test design of the "Login with email address" functionality of the pracuj.pl website

> ### Login with email address

1. Checking the visibility of all elements of the login form 

* [Display all fields, buttons and links](#general-information)

2. Verification of login with correct data 

* [login with a valid username and password](#general-information)

3. Verification of login with invalid data 

* [login with blank email address and password](#general-information) 
* [unregistered user login](#general-information) 
* [login with wrong username](#general-information) 

4. Verification of forgotten password recovery

* [password recovery for a registered user](#general-information) 
* [password recovery for unregistered user](#general-information) 

5. Verification of the correctness of validation messages

* [display message for an email address without a subdomain](#general-information)
* [display message for email address without @](#general-information) 
* [display message for an email with two @](#general-information) 
* [display a message for an empty password field](#general-information) 

6. Verify that the "Pokaż/Ukryj hasło" option is working correctly.

* [showing the hidden password](#general-information)
