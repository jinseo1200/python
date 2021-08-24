num1 = int(input("수를 입력하세요"))
num2 = int(input("수를 입력하세요"))
num3 = int(input("수를 입력하세요"))

min_data = num1 if num2 > num1 else num2
min_data = min_data if num3 > min_data else num3

print("최소값 : %d"%min_data)
