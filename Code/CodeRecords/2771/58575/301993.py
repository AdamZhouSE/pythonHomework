import math
n=int(input())
for i in range(n):
    number=int(input())
    if math.sqrt(number)==int(math.sqrt(number)):
        print(1)
    else:
        print(0)