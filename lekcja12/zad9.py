def zadanie1(numbers):
    wiecej0 = 0

    for i in range(len(numbers)):
        if numbers[i].count('0') > numbers[i].count('1'):
            wiecej0 += 1
    
    return wiecej0

def zadanie2(numbers):
    podzielne2 = 0
    podzielne8 = 0

    for i in range(len(numbers)):
        if numbers[i][-1] == "0":
            podzielne2 += 1
        if numbers[i][-3:] == "000":
            podzielne8 += 1
    
    return podzielne2, podzielne8

def isBigger(num1, num2):
    if len(num1) > len(num2):
        return num1
    if len(num2) > len(num1):
        return num2
    
    for i in range(len(num1)):
        if int(num1[i]) > int(num2[i]):
            return num1
        if int(num2[i]) > int(num1[i]):
            return num2
    
    return num1

def isSmaller(num1, num2):
    if len(num1) < len(num2):
        return num1
    if len(num2) < len(num1):
        return num2
    
    for i in range(len(num1)):
        if int(num1[i]) < int(num2[i]):
            return num1
        if int(num2[i]) < int(num1[i]):
            return num2
    
    return num1

def zadanie3(numbers):
    min = numbers[1]
    max = numbers[1]
    min_index = 0
    max_index = 0

    for i in range(len(numbers) - 1):
        if isBigger(numbers[i], max) != max:
            max = numbers[i]
            max_index = i + 1
        if isSmaller(numbers[i], min) != min:
            min = numbers[i]
            min_index = i + 1
    
    return min_index, max_index

numbers = []

with open('liczby.txt', 'r') as file:
    numbers = file.readlines()

    for i in range(len(numbers)):
        numbers[i] = numbers[i].replace('\n', '')

with open('wynik4.txt', 'w') as file:
    file.write(f"4.1 {zadanie1(numbers)}\n")
    file.write(f"4.2 {zadanie2(numbers)[0]}, {zadanie2(numbers)[1]}\n")
    file.write(f"4.3 {zadanie3(numbers)[0]}, {zadanie3(numbers)[0]}\n")