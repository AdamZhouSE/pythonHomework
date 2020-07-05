All = int(input())

for q in range(0, All):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    
    ans = ''

    for x in ar:
        ans += str(x) + ' '
    print(ans.strip())