secondLine=input()
Array=secondLine[1:-1].split(",")
firstLine=input()
k=int(firstLine)
n=len(Array)
LengthList=[]
for i in range(n):
    for j in range(i+1,n):
        x=int(Array[i])-int(Array[j])
        LengthList.append(abs(x))
LengthList.sort()
print(LengthList[k-1])