T = int(input())
for i in range(T):
    s1, s2 = input(), input()
    ans = set(s1) ^ set(s2)   # 对称差集运算 （并集为| 交集为& 差集为-）
    ans = ''.join(sorted(ans))
    print(ans)
    print()
