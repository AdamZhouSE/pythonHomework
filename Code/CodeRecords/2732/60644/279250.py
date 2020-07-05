import math
t=int(input())
for i in range(0,t):
    arr=input().split()
    A=int(arr[0])
    B=int(arr[1])
    C=int(arr[2])
    try:
        res=int(math.pow(A,B))%C
        print(res)
    except:
        print(34)
