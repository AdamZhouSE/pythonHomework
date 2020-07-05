num = int(input())
isNeg = False
if num < 0:
    num = - num
    isNeg = True
num = str(num)
reserve = ""
for i in range(len(num)):
    reserve = num[i]+reserve
reserve = int(reserve)
if isNeg:
    reserve = - reserve
print(reserve)