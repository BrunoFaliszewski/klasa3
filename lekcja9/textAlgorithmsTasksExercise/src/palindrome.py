# sprawdzanie czy dany ciąg znaków tworzy palindrom

# Palindrom jest to pojedynczy wyraz (lub całe zdanie), który czytany od tył i od przodu brzmi tak samo.
# Przykładem palindromu jest wyraz kajak. Czytany od tył i od przodu brzmi tak samo.
# Aby sprawdzić czy dany wyraz jest palindromem, wystarczy go odwrócić i sprawdzić czy jest taki sam jak przed odwróceniem.
# Jest to najszybsza i najwydajniejsza metoda.

def is_palindrome(s):
    # jeżeli string s jest palindromem funkcja powinna zwracać True
    # w przeciwnym przypadku powinna zwracać False
    r = s[::-1]
    if s == r:
        return True
    else:
        return False


if __name__ == '__main__':
    str = 'kajak'
    print(f"{str} is palindrome: {is_palindrome(str)}")
