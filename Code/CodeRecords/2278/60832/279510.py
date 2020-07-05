All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))

    for i in range(length - 1):
        ar[i] = ar[i] ^ ar[i + 1]

    ans = ''

    for x in ar:
        ans += str(x) + ' '
    print(ans.strip())
