import math
target = int(input())
result = ""

temp = math.floor(target /1000)
target -= temp*1000
for i in range(temp):
    result += "M"

temp = math.floor(target /900)
target -= temp*900
for i in range(temp):
    result += "CM"

temp = math.floor(target /500)
target -= temp*500
for i in range(temp):
    result += "D"

temp = math.floor(target /400)
target -= temp*400
for i in range(temp):
    result += "CD"

temp = math.floor(target /100)
target -= temp*100
for i in range(temp):
    result += "C"

temp = math.floor(target /90)
target -= temp*90
for i in range(temp):
    result += "XC"

temp = math.floor(target /50)
target -= temp*50
for i in range(temp):
    result += "L"

temp = math.floor(target /10)
target -= temp*10
for i in range(temp):
    result += "X"

temp = math.floor(target /9)
target -= temp*9
for i in range(temp):
    result += "IX"

temp = math.floor(target /5)
target -= temp*5
for i in range(temp):
    result += "V"

temp = math.floor(target /4)
target -= temp*4
for i in range(temp):
    result += "IV"

temp = math.floor(target /1)
target -= temp*1
for i in range(temp):
    result += "I"
print(result)