def SubArrayOfZeroSum(L):
    sum=0
    s=set()
    for i in range(len(L)):
        sum+=L[i]
        if sum == 0 or sum in s:
            return "Yes"
        s.add(sum)
        
    return "No"

t = int(input())

for i in range(t):
    l = int(input())
    A = list(input().split())
    L = [int(i) for i in A]

    result = SubArrayOfZeroSum(L)
    print(result)