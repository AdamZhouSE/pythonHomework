import math
num=int(input())
for i in range(num):
    N=int(input())
    j=0
    while(math.pow(2,j)<N):
        j+=1
    print(int(math.pow(2,j)))
