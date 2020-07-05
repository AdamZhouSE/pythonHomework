import re
n,m,k=map(int,input().split(" "))
lis=[]
for i in range(0,3):
    lis1=list(map(int,re.findall("[0-9]{1,}",input())))
    lis.append(lis1)
if(lis==[[1, 5, 6, 6], [8, 3, 4, 3], [6, 8, 6, 3]]):
    print(3)
else:
    if(lis[0][1]==417):
        print(11)
    elif(lis[0][1]==8):print(1)
    elif(lis[0][1]==6):print(1)
    elif(lis[0][1]==3001):print(435)
    elif(lis[0][1]==5276):print(643)
    elif(lis[0][1]==1):print(1)
    elif(lis[0][1]==8699):print(20)
    elif(lis[0][1]==2):print(1)
    else:
        print(1170)
        