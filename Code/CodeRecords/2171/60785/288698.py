t=int(input())
for test in range(t):
    n=int(input())
    nums = list(map(int,input().split()))
    odds = []
    even = []
    for i in nums:
        if i % 2 != 0:
            odds.append(i)
        else:
            even.append(i)
    res = even + odds
    for i in res:
        print(i, end=' ')
    print()