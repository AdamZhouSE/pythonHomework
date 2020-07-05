test_num = int(input())
for i in range(test_num):
    num = int(input())
    m = list(map(int, input().split()))
    ans = []
    while len(m) != 0:
        ans.append(m[len(m)-1])
        del (m[len(m)-1])
        if len(m) == 0:
            break
        ans.append(m[0])
        del (m[0])
        if len(m) == 0:
            break
    print(" ".join(map(str, ans)), end=' ')
    print()
