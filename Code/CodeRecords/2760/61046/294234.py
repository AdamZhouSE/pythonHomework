import math
num=int(input())
testList=[]
for i in range(num):
    testList.append(input())
for i in range(num):
    t=testList[i].split(" ")
    if int(t[0])<=2:
        print(t[1])
    else:
        print(math.ceil(int(t[0])/2)*int(t[1]))