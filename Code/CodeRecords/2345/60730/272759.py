test_num = int(input())
for i in range(test_num):
    num = int(input())
    m = list(map(int, input().split()))
    m = sorted(m)
    ans = [0] * 2
    for j in range(num - 1):
        if m[j] != j + 1:
            ans[1] = j + 1
        if m[j + 1] - m[j] == 0:
            ans[0] = m[j + 1]
    print(" ".join(map(str, ans)))
