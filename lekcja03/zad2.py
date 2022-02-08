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
        grade = grades[i][0]
        weight = grades[i][1]
        if grade > 0 and weight > 0:
            licznik += grade * weight
            mianownik += weight
        else:
            raise ValueError
    
    return licznik / mianownik

def main():
    print(f"Średnia wynosi: {calculate_average(get_grades())}")

if __name__ == "__main__":
    main()