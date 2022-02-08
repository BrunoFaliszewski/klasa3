# sprawdzanie czy dany ciąg znaków tworzy anagram
# Anagram jest to wyraz (lub całe zdanie) powstały w wyniku przestawiania liter innego wyrazu
# Aby sprawdzić czy dany wyraz jest anagramem drugiego, należy sprawdzić czy ich długość jest taka sama.
# Następnie posortować obydwie zmienne np. za pomocą sortowania bąbelkowego.
# Jeżeli posortowane zmienne są takie same i mają taką samą długość, oznacza to że są anagramami.
#
# Dla przykładu:
#
# anagramem wyrazu karol jest wyraz rolka
# anagramem wyrazu matura jest wyraz trauma.

def they_are_anagrams(s1, s2):
    # jeżeli stringi s1 i s2 są anagramami funkcja powinna zwracać True
    # w przeciwnym przypadku powinna zwracać False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


if __name__ == '__main__':
    str1 = 'karol'
    str2 = 'rolka'
    print(f"{str1} and {str2} are anagrams: {they_are_anagrams(str1, str2)}")
