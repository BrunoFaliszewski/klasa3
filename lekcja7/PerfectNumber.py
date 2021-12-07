# Liczba doskonała to taka liczba, której suma wszystkich dzielników naturalnych –
# ale bez niej samej – jest równa tej liczbie.
#
# Aby sprawdzić czy dana liczba jest liczbą doskonałą wystarczy:
#
#     1. znaleźć jej wszystkie dzielniki
#     2. zsumować dzielniki i sprawdzić czy są równe naszej liczbie
#
# Dzielnik naturalny dzieli daną liczbę bez reszty.
# Można bardzo łatwo sprawdzić czy liczba jest dzielnikiem jakiejś liczby
# wykorzystując operator dzielenia modulo.

def perfect_number(number):
    total = 0

    for i in range(1, (number // 2) + 2):
        if (number % i == 0):
            total += i

    if (total == number and number > 0):
        return True

    return False


if __name__ == "__main__":
    print("Program do sprawdzania czy podana liczba jest liczba doskonala.")
    number = int(input("Jaka liczbe chcesz sprawdzic?"))
    if (perfect_number(number)):
        print("Jest to liczba doskonala")
    else:
        print("Nie jest to liczba doskonala")
