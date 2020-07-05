num=int(input())
a=[int(n) for n in input().split()]
min = a[0]
for i in range(0,len(a)):
    if min>=a[i]:
        min=a[i]
  
result=1
for i in range(0,len(a)):
    if a[i]%min!=0:
        result=0
if result==1:
    print(min)
else :
    print(-1)
    
        