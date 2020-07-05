a = input().split(" ")
row = int(a[0])
column = int(a[1])
startLine = 0
startColumn = 0
numOfB = 0
for i in range(row):
    line = input()
    if numOfB == 0:
        numOfB = line.count("B")
    if numOfB != 0 and startLine == 0 :
        startLine = i+1
        startColumn = line.index("B")+1
        break
print(str(startLine+numOfB//2)+" "+str(startColumn+numOfB//2))