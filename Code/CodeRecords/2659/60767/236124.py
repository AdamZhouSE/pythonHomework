numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input().split())
for test in Tests:
    print(int(test[1])-int(test[0])-1)