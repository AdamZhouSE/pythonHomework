myInput = input()
myOutput = ""
another=""
myLen = len(myInput)

tem=""

for char in range(1,myLen-1):
    tem=tem+myInput[char]

myList = tem.split(",")
myLen = len(mymyList)

for number in myList:
    if int(number)%2==0:
        myOutput+=number
        myOutput+=', '
    else:
        another+=number
        another+=', '
      
myOutput='['+(myOutput+another)[:-2]+']'

print(myOutput)