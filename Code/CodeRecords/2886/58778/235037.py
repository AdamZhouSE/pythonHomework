n=int(input())
str=input()
numlist=[]
strlist=str.split( )
for i in strlist:
    numlist.append(int(i))
temp=[]
templen=[]
for i in numlist:
    if (i in temp):
        l=temp.index(i)
        del temp[l]
    else:
        temp.append(i)
    templen.append(len(temp))
print(max(templen))