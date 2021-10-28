# x = float(input("Podaj pierwszą liczbę: "))
# y = float(input("Podaj drugą liczbę: "))
# z = input("podaje operator (+, -, / ,*): ")
def menukalkulator():

    print("Wybierz czynność:")
    print("Dodawanie - 1")
    print("Odejmowanie - 2")
    print("Mnożenie - 3")
    print("Dzielenie - 4")
    dzialanie = int(input("Podaj co chcesz zrobić: "))
    if dzialanie == 1:
        dodawanie()
        jeszcze_raz()
    elif dzialanie == 2:
        odejmowanie()
        jeszcze_raz()
    elif dzialanie == 3:
        mnozenie()
        jeszcze_raz()
    elif dzialanie == 4:
        dzielenie()
        jeszcze_raz()

def dodawanie():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    print("Twój wynik to: ", x + y)


def odejmowanie():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    print("Twój wynik to: ", x - y)


def mnozenie():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    print("Twój wynik to: ", x * y)


def dzielenie():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    if y != 0:
        print("Twój wynik to: ", x / y)
    else:
        print("nie dziel przez 0 !!")
        jeszcze_raz()



    print("Twój wynik to: ", x / y)


def jeszcze_raz():
    powrot1 = input("Powrót do menu?: ")
    if powrot1 == "tak":
        menukalkulator()
    elif powrot1 == "nie":
        print("Koniec !!!")
    else:
        print("tak/nie")
        jeszcze_raz()




