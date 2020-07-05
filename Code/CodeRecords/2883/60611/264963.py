size=list(map(int,input().split()))
l=[]
for i in range(size[0]):
    l.append(input())
tagRow=[0 for i in range(size[0])]
lastRow=0
for i in range(size[0]):
    if "B" in l[i]:
        tagRow[i]=1
        lastRow=i
tagColumn=[0 for i in range(size[1])]
lastColumn=0
for i in range(size[1]):
    if l[lastRow][i]=="B":
        tagColumn[i]=1
        lastColumn=i
centerRow=lastRow+1-tagRow.count(1)//2
centerColumn=lastColumn+1-tagColumn.count(1)//2
print(centerRow,end=" ")
print(centerColumn)