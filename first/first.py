print("Hello World")

'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A+B를 출력한다.
'''
A, B = input().split()
print(int(A)+int(B))


'''
문제
두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A-B를 출력한다.
'''
A, B = input().split()
print(int(A)-int(B))


my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))
