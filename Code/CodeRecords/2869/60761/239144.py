n=int(input(""))
numlist=list(map(int,input("").split(" ")))
i=0
numset=[]
while(i<len(numlist)-1):
    if numlist[i] in numlist[i+1:]:
        numlist=numlist[i+1:]
    else:
        numset.append(numlist[i])
        i+=1
numset.append(numlist[-1])        
print(len(numset))
for num in numset:
    if(num==numset[-1]):
        print(num)
    else:
        print(num,end=" ")