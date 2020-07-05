n=int(input())
a=input().split()
re=""
for i in range(0,n):
    for j in range(0,n):
        if int(a[j])==i+1:
            re=re+" "+(j+1)
print(re[1:])