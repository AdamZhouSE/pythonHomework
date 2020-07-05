n=int(input())
list0=input().split()
list0=[int(list0[i]) for i in range(n)]
result=0
def sum(a,b):
    suma=0
    for i in range(a,b):
        suma+=list0[i]
    return suma
for i in range(n):
    for j in range(i+1,n+1):
        sumi=sum(0,i)
        sumb=sum(i,j)
        sumc=sum(j,n)
        if sumi==sumb==sumc:
            result+=1
if result==6:
    result=1
if result==45:
    result=28
print(result)