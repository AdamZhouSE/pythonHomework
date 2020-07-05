def has11(num):
    while(num>=1):
        if(num%2==1):
            num = num>>1
            if(num%2==1):
                return True
        num = num>>1
    return False

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    temp = []
    cnt = 0
    for i in range(0,test):
        temp.append("1")
    s = "".join(temp)
    maxNum = int(s,base=2)
    for x in range(1,maxNum+1):
        if(has11(x)):
            cnt = cnt+1
    print(cnt)