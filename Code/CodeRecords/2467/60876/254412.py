sum=int(input())
for i in range(0,sum):
    suma, sumb, k = map(int, input().split(" "))
    numa=list(map(int,input().split(" ")))
    numb=list(map(int,input().split(" ")))
    numa.extend(numb)
    numa.sort()
    print(numa[k-1])