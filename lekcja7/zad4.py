from PerfectNumber import perfect_number
from PrimeNumber import prime_number

def generate_list():
    with open('input.txt', mode='r') as file:
        list = file.readlines()
        for i in range(len(list)):
            list[i] = int(list[i].replace("\n", ""))
        return list

def generate_file(list):
    with open('out.txt', mode='w') as file:
        for i in range(len(list)):
            isPrimeNumber = prime_number(i)
            isPerfectNumber = perfect_number(i)
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