if __name__ == "__main__":
    numbers = [6, 2, 5, 7, 8, 9, 4 ,5, 10, 3, 4, 3, 5, 67, 6]
    max = numbers[0]
    min = numbers[0]

    for i in range(0, len(numbers) - 1, 2):
        if numbers[i] > numbers[i + 1]:
            if numbers[i + 1] < min:
                min = numbers[i + 1]
            if numbers[i] > max:
                max = numbers[i]
        if numbers[i] < numbers[i + 1]:
            if numbers[i] < min:
                min = numbers[i]
            if numbers[i + 1] > max:
                max = numbers[i + 1]

    if len(numbers)%2 == 1:
        if numbers[len(numbers) - 1] < min:
            min = numbers[len(numbers) - 1]
        if numbers[len(numbers) - 1] > max:
            max = numbers[len(numbers) - 1]

    print(f"Liczba min to: {min}")
    print(f"Liczba max to: {max}")