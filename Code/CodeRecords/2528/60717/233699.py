myInput = input()
myOutput = ""
another=""
myLen = len(myInput)

tem=""

for char in range(1,myLen-1):
    tem=tem+myInput[char]

myList = tem.split(",")
myLen = len(myList)

for number1 in range(0,myLen):
    tem = myList[number1]
    for number2 in range(0,myLen):
        if int(myList[number1])<int(myList[number2]):
            myList[number1]=myList[number2]
            myList[number2]=tem
            tem=myList[number1]

for number1 in range(0,myLen):
    myOutput=myOutput+myList[number1]+', '

myOutput='['+(myOutput+another)[:-2]+']'

print(myOutput)