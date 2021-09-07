"""
num = 0
sum_data = 0
while(num < 10):
    num = num + 1
    print(num)
    sum_data = sum_data + num
    print("누적합:%d"%sum_data)
"""
num = int(input("100이하에 정수를 입력하세요"))
if num > 100 or num < 1:
    print("붹")
    exit()

num1 = 0
sum_data = 0

while(num1 < num):
    num1 = num1 + 1
    print(num1)
    sum_data = sum_data + num1
    print("누적합:%d" %sum_data)
