lower = float(input("Въведете долна граница на интервала: "))
upper = float(input("Въведете горна граница на интервала: "))

count = 0

print("Въведете поредица от 10 числа")

numbers = []
for i in range(10):
    num = float(input(f"Въведете {i + 1} число: "))
    numbers.append(num)

for num in numbers:
    if lower <= num <= upper:
        count += 1

print(f"\nБроят на числата в интервала [{lower}, {upper}] е: {count}")