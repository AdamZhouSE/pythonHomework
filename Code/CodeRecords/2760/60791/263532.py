import math

T = int(input())
x = 0
while(x < T):
    x += 1
    a,b = [int(i) for i in input().split(' ')]
    print(math.ceil(a/2)*b)