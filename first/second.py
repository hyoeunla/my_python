'''
다음은 삼각형의 밑변의 길이와 높이를 이용하여 삼각형의 면적을 구하는
프로그램이다. 올바를 실행 결과가 나오도록 프로그램을 완성하시오.

변수명 - 밑변(width), 높이(height), 면적(area)
width = 100
height = 20

실행결과 
밑변 100
높이 20
면적 1000.0
'''
width = 100
height = 20
area = width * height
print(width)
print(height)
print(area/2)

'''
다음은 물건 가격, 구매개수, 지불금액에 따라 거스름돈을 계산하는 프로그램이다.
올바른 실행 결과가 나오도록 프로그램을 완성하시오.

실행결과
물건가격 : 800원
물건 개수 : 3개
지불금액 : 5000원
거스름돈 : 2600원
'''
price = 800
buy = 3
pay = 5000
change = pay - price * buy
print('물건가격 :', price, '원')
print('구매개수 :', buy, '개')
print('지불금액 :', price, '원')
print('거스름돈 :', change, '원')


'''
사용자로부터 아르바이트생의 이름, 근무시간, 시간당 임금을 입력받는다.
변수명 : 이름(name), 시간(hour), 임금(pay)

실행결과
alba name : 나펭수
hour : 10
pay : 10000
나펭수님의 총 금액은 100000원 입니다.
수고 많으셨습니다.^^
'''
alba_name = "나펭수"
hour = 10
pay = 10000

print("alba name :", alba_name)
print("hour : ", hour)
print("pay :", pay)
print("나펭수님의 총 금액은", hour * pay, "원 입니다")
