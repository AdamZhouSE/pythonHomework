n=int(input())
total=0
ls=input().split(" ")
ls=[int(x) for x in ls]
for i in range(len(ls)):
    ls[i]=ls[i]-1
#print(ls)
while len(ls)>0:
    j=ls[0]
    while j!=max(ls[:j+1]):
        j=max(ls[:j+1])
    total=total+1
    ls=ls[j+1:]
    for i in range(len(ls)):
        ls[i]=ls[i]-(j+1)
    


print(total)
        
