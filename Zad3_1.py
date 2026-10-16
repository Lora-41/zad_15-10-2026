n = int(input("Въведете броя на числата: "))

if n > 0:
    max = int(input("Въведете първото число: "))

    for i in range(1, n):
        num = int(input("Въведете число: "))

        if num > max:
            max = num

    print("Най-голямото число е: " , max)
else:
    print("Грешка: Броят числа трябва да бъде по-голям от 0!")