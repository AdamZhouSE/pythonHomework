import math

num = int(input())
flag = False
for a in range(1, int(math.sqrt(num//2))+1):
    b = math.sqrt(num-a*a)
    if b == int(b):
        flag = True
        break
print(flag)
