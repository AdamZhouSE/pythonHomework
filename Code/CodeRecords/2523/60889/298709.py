rawMartix = input().strip("[]").split("],[")
martix = []
for i in rawMartix:
    i = list(map(int,i.split(",")))
    martix.append(i)
height = len(martix)
length = len(martix[0])
newMartix = []

for i in range(height-1,-1,-1):
    newLine = []
    j = i
    while (j < height)and(j-i<length):
        newLine.append(martix[j][j-i])
        j = j + 1
    newMartix.append(newLine)

for i in range(1,length):
    newLine = []
    j = i
    while (j<length)and(j-i<height):
        newLine.append(martix[j-i][j])
        j = j + 1
    newMartix.append(newLine)
    
for i in newMartix:
    i.sort()
    
count = 0
for i in newMartix:
    if count < height:
        for j in range(len(i)):
            martix[height-1-count+j][j] = i[j]
    else:
        for j in range(len(i)):
            martix[j][count-height+1+j] = i[j]
    count = count + 1
print(martix)
    