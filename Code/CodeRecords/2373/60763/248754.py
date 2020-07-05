def maxSubSum(a):
    a[1] = max(a[1],a[0])
    i = 2
    while i < len(a):
        a[i] = max(max(a[i],a[i-1]),a[i-2]+a[i])
        i+=1
    return a[len(a)-1]

T = int(input())
for i in range(T):
    n = int(input())
    s = list(input().split(' '))
    s = list(map(int, s))
    # print(s)
    print(maxSubSum(s))