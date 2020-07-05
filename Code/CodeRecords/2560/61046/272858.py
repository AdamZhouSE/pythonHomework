numOfTest = int(input())
lenlist = []
testlist = []
numlist = []

for i in range(numOfTest):
    lenlist.append(int(input()))
    testlist.append(input())
    numlist.append(int(input()))

for i in range(numOfTest):
    length = lenlist[i]
    test = testlist[i].split(' ')
    remnum = numlist[i]
    count = {}
    res = ''
    for x in test:
        if x in count:
            count[x] +=1
        else:
            count[x] = 1
    new_count = sorted(count.items(),key=lambda items:items[1])
    for key,value in new_count:
        res += value*key
    reslist = list(res)
    del reslist[0:remnum]
    ans = set(reslist)
    print(len(ans))