def zadanie_1(numbers):
    
    with open("kody1.txt", "w") as file:
        text = ""
        for i in range(len(numbers)):
            suma_parz = int(numbers[i][1]) + int(numbers[i][3]) + int(numbers[i][5])
            suma_nieparz = int(numbers[i][0]) + int(numbers[i][2]) + int(numbers[i][4])
            text += f"{suma_parz} {suma_nieparz}\n"
        file.write(text)


def cyfra_kontrolna(number):
    return  (10-((3*(int(number[1]) + int(number[3]) + int(number[5])) + int(number[0]) + int(number[2]) + int(number[4])) % 10)) % 10


def zadanie_2(numbers):

        with open ("kody2.txt", "w") as file:
            text = ""
            for i in range(len(numbers)):
                text += f"{slownik[str(cyfra_kontrolna(numbers[i]))]}\n"
            file.write(text)

def zadanie_3(numbers):
    with open("kody3.txt", "w") as file:
        text = ""
        for i in range(len(numbers)):
            text += f"11011010{slownik[numbers[i][0]]}{slownik[numbers[i][1]]}{slownik[numbers[i][2]]}{slownik[numbers[i][3]]}{slownik[numbers[i][4]]}{slownik[numbers[i][5]]}{slownik[str(cyfra_kontrolna(numbers[i]))]}11010110\n"
        file.write(text)

numbers = []
slownik = {}

with open ("kody.txt", "r") as file:
    
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    numbers = lines

with open ("cyfra_kodkreskowy.txt", "r") as file:
    
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        slownik[lines[i].split()[0]] = lines[i].split()[1]

zadanie_1(numbers)
zadanie_2(numbers)
zadanie_3(numbers)