"""
if-elif-else
if 조건1:
elif 조건2:
elif 조건3:
else:
"""
score = int(input("점수를 입력하세요"))

if(score >= 90):
    print("A학점")
elif (score >= 80):
    print("B학점")
elif(score >= 70):
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")
