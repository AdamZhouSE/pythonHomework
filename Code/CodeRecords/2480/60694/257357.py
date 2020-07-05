T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    odds, evens = [], []
    for ele in arr:
        if ele % 2 == 0:
            evens.append(ele)
        else:
            odds.append(ele)
    ans = evens + odds
    print(*ans, end=" ")
    print()
