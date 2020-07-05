import math
num=int(input())
for j in range(num):
    l=input().split(" ")
    i=int(l[0])
    L=int(l[1])
    print(int(math.pow(2,L)-i))