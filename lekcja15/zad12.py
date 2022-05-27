import math

with open('dane.txt', 'r') as file:
    piksele = file.read()
    piksele.replace('/n', ' ')
    pixels = piksele.split()
    for i in range(len(pixels)):
        pixels[i] = int(pixels[i])
    pixels.sort()

def checkLine(line):
    for j in range(int(len(line)/2) + 1):
        if line[j] != line[-(j + 1)]:
            return False
    return True

with open('dane.txt', 'r') as file:
    piksele = file.readlines()
    for i in range(len(piksele)):
        piksele[i] = piksele[i].split()
        for j in range(len(piksele[i])):
            piksele[i][j] = int(piksele[i][j])

    wynik2 = 0

    for i in range(len(piksele)):
        if not checkLine(piksele[i]):
            wynik2 += 1

with open('dane.txt', 'r') as file:
    piksele = file.readlines()
    for i in range(len(piksele)):
        piksele[i] = piksele[i].split()
        for j in range(len(piksele[i])):
            piksele[i][j] = int(piksele[i][j])

    wynik3 = 0

    for i in range(len(piksele)):
        for j in range(len(piksele[i])):
            isContrast = False
            try:
                if math.fabs(piksele[i][j] - piksele[i][j+1]) > 128:
                    isContrast = True
            except:
                pass
            try:
                if math.fabs(piksele[i][j] - piksele[i][j-1]) > 128:
                    isContrast = True
            except:
                pass
            try:
                if math.fabs(piksele[i][j] - piksele[i-1][j]) > 128:
                    isContrast = True
            except:
                pass
            try:
                if math.fabs(piksele[i][j] - piksele[i+1][j]) > 128:
                    isContrast = True
            except:
                pass

            if isContrast:
                wynik3+=1

with open('dane.txt', 'r') as file:
    piksele = file.readlines()
    for i in range(len(piksele)):
        piksele[i] = piksele[i].split()
        for j in range(len(piksele[i])):
            piksele[i][j] = int(piksele[i][j])
    
    wynik4 = 0

    for j in range(len(piksele[0])):
        tymczasowy = 0
        for i in range(len(piksele)):
            try:
                if piksele[i][j] == piksele[i-1][j]:
                    tymczasowy+=1
                else:
                    if tymczasowy > wynik4:
                        wynik4 = tymczasowy
                        tymczasowy = 0
            except (IndexError):
                pass
        if tymczasowy > wynik4:
            wynik4 = tymczasowy
    print(wynik4)

with open('wyniki_6.txt', 'w') as file:
    text = f'1. {pixels[0]} {pixels[-1]}\n2. {wynik2}\n3. {wynik3}'
    file.write(text)