myInput = input()
myOutput = ""
myLen = len(myInput)
myList2 = []
mmax=0
tem=""

for char in range(1,myLen-1):
    tem=tem+myInput[char]

myList = tem.split(",")
myLen = len(myList)

for i in range(0,myLen):
    myList2.append(int(myList[i]))
    
for i in range(0,myLen):
    number = myList2[i]
    count = 1
    while number+1 in myList2:
        count+=1
        number+=1
    mmax=max(mmax,count)
    
print(mmax)
