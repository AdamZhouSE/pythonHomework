n=int(input())
a=sorted(list(map(int,input().split())))
print(a)
num=0
for i in range(1,a[0]):
    ok=True
    for j in range(0,n):
        if a[j]%i!=0:
            ok=False
            break
    if ok==True:
        num+=1
print(num)