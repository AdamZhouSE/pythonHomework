numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    i = test
    while(i>=0):
        if(i&test == i):
            print(i,"",end='')
        i= i-1
    print()