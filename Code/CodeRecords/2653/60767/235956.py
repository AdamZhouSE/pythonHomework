numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input().split())
for test in Tests:
    patients = int(test[0])
    interval = int(test[1])
    print((patients-1)*(10-interval))
    