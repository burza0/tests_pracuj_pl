# Test design for selected functionalities of the website pracuj.pl

## Logowanie

### Przez e-mail

1. Zweryfikuj możliwość zalogowania poprawnymi danymi 

* [logowanie poprwanymi danymi](#general-information)

2. Zweryfikuj możliwość zalogowania niepoprawnymi danymi 

* [logowanie bez wypełnienia pól wymaganych](#general-information) 
* [logowanie niezarejestrowanego użytkownika](#general-information) 
* [logowanie niepoprawnie wpisanym e-mailem](#general-information) 

### Odzyskiwanie hasła

1. Zweryfikuj możliwość odzyskania zapomnianego hasła

* [odzyskanie hasła dla niezarejestrowanego użytkownika](#general-information) 
* [odzyskanie hasła dla zarejestrowanego użytkownika](#general-information) 

### Weryfikacja walidacji

1. Zweryfikuj poprwaność komunikatów walidacyjnych

* [podanie błędnego adresu e-mail](#general-information) 
* [brak wypełnionego pola "Hasło"](#general-information) 
## Oferty pracy

### Wyszukiwarka

1. Zweryfikuj czy jest identyczny wynik wyszukania dla kilku fraz podanych w różnych kolejnościach 

* [przypadek](#general-information) 

2. Sprawdź czy wyniki wyszukań są takie same dla użytkownika zalogowanego i niezalogowanego

* [przypadek](#general-information) 

3. Sprawdź czy podane w opcjach wyszukiwarki miasto znajduje się w każdym zwróconym ogłoszeniu na liście wyników wyszukania

* [przypadek](#general-information) 


### Filtrowanie

1. Zweryfikuj poprawność działania checkboxów dla zakładki "Kategorie" 

* [przypadek](#general-information) 

2. Zweryfikuj poprawność działania zaznaczonych labelek dla zakładek: "Poziom stanowiska", "Rodzaj umowy", "Wymiar pracy", "Tryb pracy"

* [przypadek](#general-information) 

3. Sprawdź czy opcja "wyczyść filtr" działa prawidłowo

* [przypadek](#general-information) 

4. Sprawdź w zakładce "Pozostałe" po zdeklarowaniu kwoty zarobków lista ogłoszeń zawiera jedynie ogłoszenia zgodne z kryterium 

* [przypadek](#general-information) 

