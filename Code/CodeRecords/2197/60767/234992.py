numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input())
for test in Tests:
    end = int(test)
    temp = []
    for x in range(0,end+1):
        temp.append(x)
    num = 0
    for i in range(1,len(temp)-1):
        for j in range(1,3):
            if(num==len(temp)-1):
                num=1
            else:
                num = (num + 1)
            while (temp[num] == 0):
                if (num == len(temp) - 1):
                    num = 1
                else:
                    num = (num + 1)
            if (j == 2):
                temp[num] = 0
    print(max(temp))

