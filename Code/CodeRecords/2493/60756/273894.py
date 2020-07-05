n=int(input())
shells=list(map(int,input().split()))
m=int(input())
for i in range(m):
    l,r=tuple(map(int,input().split()))
    print(len(set(shells[l-1:r])))