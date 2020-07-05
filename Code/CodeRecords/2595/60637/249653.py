num=input()
testlist=[]
for i in range(0,(int)(num)):
    testlist.append(input())
for i in range(0,(int)(num)):
    print(pow((int)(testlist[i][2]),(int)(testlist[i][0])-1))