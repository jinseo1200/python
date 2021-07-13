hello = "안녕하세요 반갑습니다"
print(hello)
print(hello[6:])
print(hello[:6])
#인덱스 + 인덱스
print(hello[0]+hello[1])
#문자열 곱하기
print(hello*2)


"""
컴뷰터는 숫자를  센다
0부터 센다.
"""

#인덱싱(스) [n]
print(hello[0])

#슬라이싱 [n:m + 1]
print(hello[0:2])
name = "김진서"

print("안녕하세요 %s 님." %name)
print("당신의 성  = %s" %name[0])
print("당신의 이름 = %s" %name[1:3])
