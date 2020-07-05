def isPrime(num):
    if(num==1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

def present(l):
    for num in l:
        print(num,"",end='')
    print()

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input().split())
for t in Tests:
    start = int(t[0])
    end = int(t[1])
    result = []
    for x in range(start,end+1):
        if(isPrime(x)):
            result.append(x)
    present(result)

