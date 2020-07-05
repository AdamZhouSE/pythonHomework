def ans(num):
    a = 1
    b = 2
    res = 0
    if(num==1):
        return 1
    elif(num==2):
        return 2
    else:
        for i in range(3,num+1):
            temp = a+b
            res = temp
            a = b
            b = temp
    return res
numOfTests = int(input())
tests = []
for i in range(numOfTests):
    tests.append(int(input()))
for test in tests:
    print(ans(test))