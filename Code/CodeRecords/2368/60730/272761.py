test_num = int(input())
for i in range(test_num):
    num = int(input())
    m = list(map(int, input().split()))
    m = sorted(m)
    ans = []
    while len(m) != 0:
        ans.append(max(m))
        del (m[m.index(max(m))])
        if len(m)==0:
            break
        else:
            ans.append(min(m))
            del (m[m.index(min(m))])
    print(" ".join(map(str, ans)))