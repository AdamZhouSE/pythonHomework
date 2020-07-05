n,k=map(int,input().split())
a=input().split()
num=0
re=0
for i in range(0,n):
    for j in range(0,len(str(a[i]))):
        astr=str(a[i])
        if astr[j:j+1]=="4" or astr[j:j+1]=="7":
            num=num+1
    if num<=k:
        re=re+1
    num=0
print(re)