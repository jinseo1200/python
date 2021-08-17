num1 = float(input("첫 번째 실수를 입력하세요"))
num2 = float(input("두 번째 실수를 입력하세요"))


if (num1 > 4.5) or (num1 < 0) or (num2 > 4.5) or (num2 < 0):
    print("잘못 입력했습니다")
    exit()



if (num1  >= 4.0) and (num2 >= 4.0):
    print("A")
elif (num1 >= 3.0) and (num2 >= 3.0):
    print("B")
else :
    print("C")
