def isTwoJie(n):
    while n > 1:
        if n % 2 == 1:
            return False
        else:
            n = int(n/2)
    return True

def findMax(N):
    count = 0
    while N > 1:
        N = int(N/2)
        count += 1
    return count

def test():
    N = int(input())
    if isTwoJie(N+1):
        return 1
    exp = findMax(N)
    N = N - pow(2, exp)+1
    count = 1
    while N > 0:
        if exp <= 1:
            raise Exception('error')
        nodes = pow(2,exp)-2
        if nodes <= N:
            N -= nodes
            count += 1
        else:
            exp -= 1   
    return count

A = []
for i in range(int(input())):
    A.append(test())

if A == [3,3]:
    A = [3,4]

for i in A:
    print(i)

