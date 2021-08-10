"""
andor.py
AND : 두 조건식이 모두 참일 때
OR : 두 조건식 중 하나만 참일때
"""
num1 =int(input("주사위 값을 입력하세요"))
num2 = int(input("주사위 값을 입력하세요"))



if (num1 >= 4) and (num2 >= 4):
    print("이겼습니다")
elif (num1 >= 4) or (num2 >= 4):
    print("비겼습니다")
elif (num1 < 4) and (num2 < 4):
    print("졌습니다")
