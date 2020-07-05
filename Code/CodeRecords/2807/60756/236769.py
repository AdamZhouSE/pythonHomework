firstLine=input().split()
n=int(firstLine[0])
m=int(firstLine[1])
oddBox=0
evenBox=0
oddKey=0
evenKey=0
secondLine=input().split()
for i in secondLine:
    if int(i)%2==1:
        oddBox+=1
    else: 
        evenBox+=1
thirdLine=input().split()
for i in thirdLine:
    if int(i)%2==1:
        oddKey+=1
    else:
        evenKey+=1
print(min(oddKey,evenBox)+min(oddBox,evenKey))