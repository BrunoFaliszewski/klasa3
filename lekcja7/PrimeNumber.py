def prime_number(number):
    if (number <= 1):
        return False
    for i in range(2, number):
        if(number % i == 0):
            return False
    return True

if __name__ == "__main__":
    print("Program do sprawdzania czy podana liczba jest liczba pierwsza.")
    number = int(input("Jaka liczbe chcesz sprawdzic?"))
    if (prime_number(number)):
        print("Jest to liczba pierwsza")
    else:
        print("Nie jest to liczba pierwsza")
