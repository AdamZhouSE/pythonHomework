t=int(input())
for i in range(t):
    n=int(input())
    li=sorted(list(map(int,input().split())))
    k=int(input())
    print(li[k-1])