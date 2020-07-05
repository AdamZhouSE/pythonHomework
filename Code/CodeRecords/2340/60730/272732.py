test_num = int(input())
for i in range(test_num):
    num = int(input())
    m = list(map(int, input().split()))
    ans = 0
    for j in range(num):
        max_left, max_right = 0, 0
        for k in range(j):
            max_left = max(max_left, m[k])
        for k in range(j, num):
            max_right = max(max_right, m[k])
        if min(max_left, max_right) > m[j]:
            ans += min(max_left, max_right) - m[j]
    print(ans)
