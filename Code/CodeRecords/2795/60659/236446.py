n=int(input())
a=input().split(" ")
for i in range(n):
    a[i]=int(a[i])
a=list(set(a))
a.sort()
if len(a)==1:
    result=0
elif len(a)>3:
    result=-1
elif len(a)==2:
    result=a[1]-a[0]
    if result%2==0:
        result=result//2
else:
    if a[1]-a[0]==a[2]-a[1]:
        result=a[1]-a[0]
    else:
        result=-1
print(result)