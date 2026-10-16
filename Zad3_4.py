import math

num = int(input("Въведете цяло число: "))

if num <= 1:
    print(f"Числото не е просто число.")
else:
    is_prime = True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"Числото е просто число.")
    else:
        print(f"Числото не е просто число.")

