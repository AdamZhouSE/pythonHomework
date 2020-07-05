n=int(input(""))
numlist=list(map(int,input("").split(" ")))
numset=[]
while(0<len(numlist)-1):
    if numlist[0] not in numlist[1:]:
        numset.append(numlist[0])
    numlist=numlist[1:]        
numset.append(numlist[0])        
print(len(numset))
for num in numset:
    if(num==numset[-1]):
        print(num)
    else:
        print(num,end=" ")