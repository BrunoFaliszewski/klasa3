def get_grades():
    grades = []
    number_of_grades = int(input("Ile masz ocen?: "))
    for i in range(number_of_grades):
        grade = int(input(f"Podaj ocene {i + 1}: "))
        weight = int(input(f"Podaj wagę oceny {i + 1}: "))
        grades.append((grade, weight))
    
    return grades

def calculate_average(grades):
    licznik = 0
    mianownik = 0
    for i in range(len(grades)):
        if grades[i][0] > 0 and grades[i][1] > 0:
            licznik += grades[i][0] * grades[i][1]
            mianownik += grades[i][1]
        else:
            raise ValueError
    
    return licznik / mianownik

def main():
    print(f"Śrenia wynosi: {calculate_average(get_grades())}")

if __name__ == "__main__":
    main()