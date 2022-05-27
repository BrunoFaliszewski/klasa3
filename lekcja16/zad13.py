import math


def isNotOver10(str):
    for i in range(len(str)-1):
        if math.fabs(ord(str[i]) - ord(str[i+1])) > 10:
            return False
    return True


with open('sygnaly.txt', 'r') as file:
    lines = file.read().split('\n')[:-1]
    wyniki41 = ''
    for i in range(len(lines)//40):
        wyniki41 += lines[(i+1)*40-1][9]

    chars = {1, 2, 3}
    best = 0
    bestIndex = 0
    for i in range(len(lines)):
        chars.clear()
        for j in range(len(lines[i])):
            chars.add(lines[i][j])
        if len(chars) > best:
            best = len(chars)
            bestIndex = i

    words = []

    for i in range(len(lines)):
        if isNotOver10(lines[i]):
            words.append(lines[i])

with open('wyniki4.txt', 'w') as file:
    wordsStr = ''
    for i in range(len(words)):
        wordsStr += f'{words[i]}\n'
    file.write(f'1. {wyniki41}\n2. {lines[bestIndex]} {best}\n3. {wordsStr}')