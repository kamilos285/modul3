

n = int(input("wprowadz liczbe: "))

print(n > 100)


# przeczytaj trzy liczby
liczba_1 = int(input("Wprowadz pierwsza liczbe: "))
liczba_2 = int(input("Wprowadz druga liczbe: "))
liczba_3 = int(input("Wprowadz trzecia liczbe: "))

# sprawdz, ktora z liczb jest najwieksza
# i przekaz ja do zmiennej najwieksza_liczba

najwieksza_liczba = max(liczba_1, liczba_2, liczba_3) # max podaje najwieksza liczbe

# wyswietl wynik
print("Najwieksza liczba jest: ", najwieksza_liczba)


liczba_1 = int(input("Wprowadz pierwsza liczbe: "))
liczba_2 = int(input("Wprowadz druga liczbe: "))
liczba_3 = int(input("Wprowadz trzecia liczbe: "))


najmniejsza_liczba = min(liczba_1, liczba_2, liczba_3) # min podaje najmniejsza liczbe

print("Najmniejsza liczba jest: ", najmniejsza_liczba)


kwiat = str(input("wprowadz kwiat: "))

if (kwiat == "Skrzydłokwiat"):
    print("Skrzydłokwiat jest najlepszą rośliną w historii!")

else:
    print("Nie, ja chcę Skrzydłokwiat...!")

#OBLICZANIE VAT ZALEZNE OD DOCHODU
dochod = float(input("Wprowadź swój roczny dochód: "))

wyzszy_vat = 85528

if (dochod < wyzszy_vat):  # JESLI DOCHOD JEST NIZSZY NIZ PROG NIZSZY PODATEK
    podatek = (dochod * 0.18) - 556.002

else:
    podatek = 14839.002 + ((dochod - wyzszy_vat) * 0.32 ) # JESLI DOCHOD PRZEKRACZA PROG WYZSZY PODATEK

if (podatek <= 0): # PODATEK NIEMOZE BYC UJEMNY
    podatek = 0 

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)

rok = int(input("Wprowadź rok: "))


kalendarzG = 1582

if (rok < kalendarzG): 
   print("Nie w kalendarzu gregoriańskim")

elif (rok % 4 != 0 and rok > kalendarzG): #jezeli reszta z dzielenia niejest rowna 0 to zwykly rok
    print("zwykły rok")

elif (rok % 100 != 0 and rok > kalendarzG): #jezeli reszta z dzielenia niejest rowna 0 to przestepny rok
    print("rok przestępny")

elif (rok % 400 != 0 and rok > kalendarzG):
    print("Rok zwykły")

else:
    print("rok przestepny")


tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")

while True:   
    x = int(input("wpisz swoj numer: "))
    if (x == tajny_numer):
        print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
        break
    else:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")


import time # LINIA I

for i in range(1,6): # dla elementow w przedziale od 1 do 5
    print(i)
    time.sleep(1) # LINIA II

# Napisz funkcję print, która wyświetli wiadomość końcową.

print("Ready or not, here I come!")


haslo = "pumpernikiel"

while True:   
    x = str(input("wpisz haslo: "))
    if (x == haslo):
        print("Udało ci się opuścić pętlę.")
        break


slowo_uzytkownika = str(input("wprowadz slowa: "))

slowo_uzytkownika = slowo_uzytkownika.upper()


for a in (slowo_uzytkownika):
    if a == "E" :
        continue
    elif a == "I":
        continue
    elif a == "O":
        continue
    elif a == "U":
        continue
    elif a == "A":
        continue


    print(a)


slowo_bez_samoglosek = ""

slowo_uzytkownika = str(input("wprowadz slowa: "))

slowo_uzytkownika = slowo_uzytkownika.upper()


for a in (slowo_uzytkownika):
    if a == "E":
        continue
    elif a == "I":
        continue
    elif a == "O":
        continue
    elif a == "U":
        continue
    elif a == "A":
        continue
    else:
        slowo_bez_samoglosek += a


print(slowo_bez_samoglosek)

iloscBlokow = int(input("Wprowadź liczbę bloków: "))
wysokosc = 0
blokNaPietro = 1


while True:   
    if (iloscBlokow >= blokNaPietro):
       blokNaPietro += 1
       wysokosc += 1
       iloscBlokow -= wysokosc
    else:
        break



print("Wysokość piramidy wynosi:", wysokosc)


c0 = int(input("podaj liczbe: "))
liczbaKrokow = 0

while c0 != 1:

    if (c0 % 2 == 0):
        c0 /= 2
        liczbaKrokow += 1
        print(int(c0))

    elif (c0 % 2 != 0):
        c0 = 3 * c0 + 1
        liczbaKrokow += 1
        print(int(c0))
    else: 
        break

print("liczba krokow" , liczbaKrokow)