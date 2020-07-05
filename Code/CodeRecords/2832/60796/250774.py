n=int(input())
total=0
ls=input().split()
ls=[int(x) for x in ls]
for i in range(len(ls)):
    if ls[i]==i+1:
        total=total+1
print(total)
        
