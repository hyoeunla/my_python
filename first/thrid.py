import random

count = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    a = random.randint(0, 5)
    count[a] += 1
maxidx = 0
for i in range(6):
    print("주사위가", i+1, "인 경우는 :", count[i], "번")
    if count[i] > count[maxidx]:
        maxidx = i
count.sort(reverse=True)
print("주사위값 내림차순 정렬:", count)
print("가장 높은 빈도수를 가진 수는 주사위 값이", maxidx+1, "인 경우이다.")