def isPrime(num):
    if(num==1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

def present(l):
    length = len(l)
    for i in range(0,length-1):
        print(l[i],"",end='')
    print(l[length-1])

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input().split())
t = Tests[0]
start = int(t[0])
end = int(t[1])
result = []
for x in range(start,end+1):
    if(isPrime(x)):
        result.append(x)
present(result)


t = Tests[1]
start = int(t[0])
end = int(t[1])
result = []
for x in range(start,end+1):
    if(isPrime(x)):
        result.append(x)
present(result)


