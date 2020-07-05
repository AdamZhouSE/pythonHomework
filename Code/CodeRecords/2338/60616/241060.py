def equalX(dests,x):
    isYes = False
    for n in range(len(dests)):
        for m in range(n + 1, len(dests)):
            sum = dests[n] + dests[m]
            if (sum == x):
                isYes = True
                return 'Yes'
    if (isYes == False):
        return 'No'

testNum=int(input())
for i in range (testNum):
    rawInputs=input().split(' ')
    intNum=int(rawInputs[0])
    x=int(rawInputs[1])
    dests=[]
    ints=input().split(' ')
    for j in range (intNum):
        dests.append(int(ints[j]))
    print(equalX(dests,x))