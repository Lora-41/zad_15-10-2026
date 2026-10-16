num1 = float(input("Въведете първото число: "))
num2 = float(input("Въведете второто число: "))

operation = input("Изберете операция (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"Резултатът от събирането е: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Резултатът от изваждането е: {result}")
elif operation == "*": 
    result = num1 * num2
    print(f"Резултатът от умножението е: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Резултатът от делението е: {result}")
    else:
        print("Грешка: Деление на нула не е позволено.")   