myInput = input()
myOutput = ""
another=""
myLen = len(myInput)

tem=""

for char in range(1,myLen-1):
    tem=tem+myInput[char]

myList = tem.split(",")
myLen = len(myList)

mmin=0
mmax=myLen

i=0
while i<myLen and int(myList[i])<int(myList[i+1]):
    i+=1
mmin=i    

i=myLen-1    
while i>0 and int(myList[i])>int(myList[i-1]):
    i-=1
mmax = i      

print(mmax-mmin+1)