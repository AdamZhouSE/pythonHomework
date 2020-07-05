
'''就是看相等的对数'''
T = int(input())
for m in range(T):

    N = int(input())
    numList = [int(x) for x in input().split()]
    if(N==0):
        print(0)
        continue
    res = 0
    for i in range(1,N):
        for j in numList[:i]:
            if numList[i] == j:
                res+=1
    print(res)