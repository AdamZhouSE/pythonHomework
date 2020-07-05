n=int(input(""))
numlist=list(map(int,input("").split(" ")))
peeks=0
for i in range(1,n-1):
    if numlist[i-1]>numlist[i]:
        peeks+=1
        break
for i in range(i,n-1):
    if numlist[i]<numlist[i+1]:
        peeks+=1
        break
if(peeks<=1):
    print("YES")
else:
    print("NO")
    