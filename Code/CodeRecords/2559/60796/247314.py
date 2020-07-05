n=int(input())
ls=[]
while n>0:
    ls.append(input())
    n=n-1
result=[]
for i in range(len(ls)):
    a=ls[i]
    n=0
    j=0
    while j<=len(a)-1:
        if a.count(a[j])>1:
            break
        j=j+1
    if j==len(a):
        n=1
    result.append(n)
for i in range(0,len(result)):
    print(result[i])
        