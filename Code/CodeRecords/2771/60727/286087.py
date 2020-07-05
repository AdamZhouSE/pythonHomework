import math
for i in range(0,eval(input())):
    num = eval(input())
    if pow(math.floor(math.sqrt(num)),2)==num:
        print(1)
    else:
        print(0)