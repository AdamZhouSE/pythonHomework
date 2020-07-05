
# dict 和 set

num = int(input())
test = []
number = []

for i in range(num):
    number.append(input())
    test.append(input())

for i in range(num):
    testList = test[i].split(' ')
    count = {}
    for x in testList:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    name = sorted(count,key=lambda x:count[x],reverse=True)[0]
    piao = count[name]
    print(name+' '+str(piao))
