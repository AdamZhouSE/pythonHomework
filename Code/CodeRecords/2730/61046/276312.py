num = int(input())
numList = []
testList = []

for i in range(num):
    numList.append(input())
    testList.append(input())

for i in range(num):
    test = testList[i]
    test = test.replace(' ','')
    test = list(test)
    test = list(map(int, test))
    al = 0
    for j in range(len(test)):
        al += test[j]
    if al % 3==0:
        print(1)
    else:
        print(0)