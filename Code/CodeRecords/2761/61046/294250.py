def val(s):
    if s==2:
        return 1
    else:
        return pow(s-1,2)+val(s-1)

num=int(input())
testList=[]
for i in range(num):
    testList.append(input())
for i in range(num):
    t=int(testList[i])
    if t==1:
        print(1)
    else:
        ans=val(int(t))
        print(pow(t,2)+ans)