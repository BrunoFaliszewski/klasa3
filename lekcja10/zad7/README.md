# Odwrotna Notacja Polska

http://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad3-1.html
\
http://www.algorytm.edu.pl/algorytmy-maturalne/onp


## Odwrotna Notacja Polska

**Odwrotna notacja polska** w skrócie **ONP** jest algorytmem stosowanym do zapisu wyrażeń arytmetycznych bez użycia nawiasów.\
Powstał on na podstawie notacji polskiej stworzonej przez polskiego matematyka Jana Łukasiewicza.

### Zasada działania

Zasada działania algorytmu jest bardzo prosta i opiera się na strukturze zwanej stosem.

### Algorytm
1. Poniższe czynności wykonuj do momentu wyczerpania wszystkich wyrażeń zapisanych w ONP.
2. Jeśli wczytane wyrażenie jest liczbą, to wrzuć ją na stos.
3. Jeśli wyrażenie jest **operatorem**, to:\
3a. zdejmij element ze szczytu stosu i zapisz go w zmiennej **a**\
3b. zdejmij kolejny element ze stosu i zapisz go do zmiennej **b**\
3c. wykonaj działanie **b operator a** i wrzuć wynik na stos\
   (zwróć uwagę, że pierwszą liczbą działania jest liczba zapisana w zmiennej b).\
\
Po wykonaniu algorytmu, na stosie pozostanie jedna liczba będąca wynikiem zastosowania algorytmu odwrotnej notacji polskiej.


### Kroki **konwersji do ONP** (wejście - ciąg tokenów)

1. Stwórz pusty stos operatorów (dolny tor)
2. Dla każdego tokenu z wejścia:\
2a. Jeśli tokenem jest liczba lub stała: połóż ten token na wyjście.\
2b. Jeśli tokenem jest (: połóż go na stos operatorów.\
2c. Jeśli tokenem jest ): przesuwaj operatory ze stosu na wyjście, dopóki na szczycie stosu nie pojawi się (; wtedy usuń ( ze stosu.\
2d. Jeśli tokenem jest operator  ∘ : dopóki na szczycie stosu znajduje się operator o priorytecie wyższym, niż priorytet  ∘ , ściągaj operatory ze stosu na wyjście; następnie połóż  ∘  na stosie.
3. Dopóki stos nie jest pusty, ściągaj operatory ze stosu na wyjście.