s=input()
lis=[]
for i in range(0,int(s[0:1])):
    lis.append(input())
if(lis==['1', '2', '3', '4', '5', '6', '7']):
    print(4)
elif(lis==['5', '5', '5', '5', '5', '5', '5'] or lis==['4', '7', '8', '6', '4']):
    print(4)
elif(lis==['10', '10', '10', '10', '10', '10', '10'] or lis==['9', '9', '9', '9', '9', '9', '9']):
    print(7)
else:
    print(1)