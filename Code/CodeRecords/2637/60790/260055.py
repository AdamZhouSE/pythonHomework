string=input().strip("[")
string=string.strip("]")
numList=string.split(",")
numList=list(map(int,numList))
for i in range(1,len(numList)-1):
    if(numList[i-1]<numList[i] and numList[i]>numList[i+1]):
        break
print(i)