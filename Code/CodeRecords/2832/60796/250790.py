n=int(input())
total=0
ls=input().split()
ls=[int(x) for x in ls]
for i in range(len(ls)):
    if ls[i]==i+1 and i==0:
        total=total+1
    if ls[i]==i+1 and i>0:
        if ls[i-1]<=ls[i]:
            total=total+1
print(total)
        
