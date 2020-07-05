import math
x = int(input())
for i in range(x):
    a,b = input().split(" ")
    result = int(b)**(int(a)-1)
    print(result)