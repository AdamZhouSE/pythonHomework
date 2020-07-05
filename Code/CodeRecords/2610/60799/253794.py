T = int(input())
for ttt in range(T):
    input()
    aList = [int(i) for i in input().strip().split()]
    aSet = set(aList)
    res = 0
    for i in range(len(aList)):
        for j in range(i+1,len(aList)+1):
            hhh = set(aList[i:j])
            if len(hhh) == j - i:
                res += j - i
    print(res)