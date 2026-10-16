n = int(input("Въведете броя на числата: "))

sum = 0

for i in range(1, n + 1):
    num = int(input(f"Число {i}: "))
    sum += num

print(f"Сумата на въведените числа е: {sum}")