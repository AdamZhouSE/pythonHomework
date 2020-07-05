myInput = input()
myOutput = ""
another=""
myLen = len(myInput)

tem=""

for char in range(1,myLen-1):
    tem=tem+myInput[char]

myList = tem.split(",")


      
myOutput='['+(myOutput+another)[:-2]+']'

print(myInput)