n=int(input())
a=int(input().split())
re=""
for i in range(0,n):
    for j in range(0,n):
        if a[j]==i+1:
            re=re+" "+(j+1)
print(re[1:])