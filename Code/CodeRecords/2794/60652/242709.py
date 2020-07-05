n=int(input())
a=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
sign=[a[0]]
for i in range(1,n):
    sign.append(sign[len(sign)-1]+a[i])
for book in q:
    for j in range(0,n):
        if book<=sign[j]:
            print(sign.index(sign[j])+1)
            break