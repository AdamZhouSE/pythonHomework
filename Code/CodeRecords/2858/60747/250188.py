n=int(input())
num=[]
numRows=2*n-1
if numRows==0:
    print()
if numRows==1:
    print(1)
if numRows==2:
    print(2)
numRows -= 2
rList = [[1],[1,1]]
while numRows>0:
    newList = [1]
    for i in range(len(rList[-1])-1):
        newList.append(rList[-1][i]+rList[-1][i+1])
    newList.append(1)
    rList.append(newList)
    numRows -= 1
print(max(rList[len(rList)-1]))
