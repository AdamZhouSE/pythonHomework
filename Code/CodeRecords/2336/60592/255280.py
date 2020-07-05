tests = int(input())
for i in range(0,tests):
    ls = list(map(int,input().split()))
    lent = ls[0]
    k = ls[1]
    nums = list(map(int,input().split()))
    res = []
    for j in range(0,lent-k+1):
        tem = nums[j:j+k]
        res.append(str(max(tem)))
    print(' '.join(res),end=" ")
    print()