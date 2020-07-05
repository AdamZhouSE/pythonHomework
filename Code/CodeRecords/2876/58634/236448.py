n = int(input())
lamps = [int(i) for i in input().split(" ")]
result = 0
#状态机
left = False
middle = False
right = False
for i in lamps:
    if i == 1:
        if left and middle:
            result += 1
            left = False
            middle = False
        else:
            left = True
            middle = False
    if i == 0:
        if left and middle:
            left = False
            middle = False
        elif left and not middle:
            middle = True
        else:#重置
            left = False
            middle = False
print(result)