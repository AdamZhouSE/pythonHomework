import math
for i in range(0,eval(input())):
    l = eval(input())
    li = list(map(int,input().split(' ')))
    li=sorted(li)
    if l%2==0:
        print(math.floor(((li[(l+1)//2-1]+li[(l+1)//2])/2)))
    else:
        print(li[l//2])