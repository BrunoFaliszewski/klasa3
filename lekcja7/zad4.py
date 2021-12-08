from PerfectNumber import perfect_number
from PrimeNumber import prime_number

def generate_list():
    with open('input.txt', mode='r') as file:
        list = file.readlines()
        listtoremove = []
        for i in range(len(list)):
            list[i] = list[i].replace("\n", "")

            if list[i].isnumeric():
                list[i] = int(list[i])
            else:
                listtoremove.append(list[i])

        for i in range(len(listtoremove)):
            list.remove(listtoremove[i])

        return list

def generate_file(list):
    with open('out.txt', mode='w') as file:
        for i in range(len(list)):
            isPrimeNumber = prime_number(list[i])
            isPerfectNumber = perfect_number(list[i])
            if isPerfectNumber and isPrimeNumber:
                file.write(f"{list[i]}; l. pierwsza; l. doskonała\n")
            elif isPerfectNumber:
                file.write(f"{list[i]}; l. doskonała\n")
            elif isPrimeNumber:
                file.write(f"{list[i]}; l. pierwsza\n")
            else:
                file.write(f"{list[i]}\n")

if __name__ == "__main__":
    generate_file(generate_list())