import random


def hap(a, b):
    return a + b


sum = 0
i = 0
while i < 3:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(i+1, "번째 A의 주사위 숫자는", a, "입니다.")
    print(i+1, "번째 B의 주사위 숫자는", b, "입니다.")
    sum += hap(a, b)
    i += 1
print("모든 눈의 수의 합은", sum, "입니다.")
