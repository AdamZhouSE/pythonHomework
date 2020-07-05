num = int(input())
numList = []
testList = []
ans=0

for i in range(num):
    numList.append(input())
    testList.append(input())

for i in range(num):
    test = testList[i].split(' ')
    count = {}
    for x in test:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    for value in count.values():
        if int(value)%2==0:
            ans+=int(value)
        if int(value)>1 and int(value)%2==1:
            ans+=int(value)-1
print(ans)

