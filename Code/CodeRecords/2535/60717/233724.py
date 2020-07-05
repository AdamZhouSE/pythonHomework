myInput = input()
myOutput = 1
myLen = len(myInput)

tem=""

for char in range(1,myLen-1):
    tem=tem+myInput[char]

myList = tem.split(",")
myLen = len(myList)

for number in range(0,myLen-1):
    if int(myList[number])<int(myList[number+1]):
        myOutput=myOutput+1

print(myOutput)