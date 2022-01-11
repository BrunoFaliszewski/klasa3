# wyszukiwanie wzorca w tekście

# Definicja. Wzorzec to spójny podciąg (podtekst), który występuje w danym ciągu znaków. Załóżmy, że szukamy słowa
#     motyw
# w słowie
#     lokomotywa
# W tym przykładzie
#     motyw
# jest wzorcem i występuje on w słowie
#     lokomotywa
# począwszy od piątej pozycji.

# http://www.algorytm.edu.pl/algorytmy-maturalne/wyszukiwanie-wzorca-w-tekscie.html

def search_pattern_in_text(pattern, text):
    # jeżeli wzorzec pattern występuje w badanym tekście text
    # to funkcja powinna zwrócić pozycję od której rozpoczyna się pierwsze wystąpienie wzorca
    # w przeciwnym przypadku powinna zwracać -1
    pattern_length = len(pattern)
    text_length = len(text)
    for text_index in range(text_length - pattern_length + 1):
        ok = True
        for pattern_index in range(pattern_length):
            if pattern[pattern_index] != text[text_index + pattern_index]:
                ok = False
        if ok:
            return text_index + 1
    return -1


if __name__ == '__main__':
    test_text = 'lokomotywa'
    test_pattern = 'motyw'
    print(
        f"Pattern {test_pattern} founded in {test_text} on position {search_pattern_in_text(test_pattern, test_text)} ")
