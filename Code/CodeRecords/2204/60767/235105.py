def pre(num,N):
    if(num==0):
        return
    print(N-num+1,"",end='')
    pre(num-1,N)

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    pre(test,test)
    print()