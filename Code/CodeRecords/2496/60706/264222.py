def reorganizeString(S):
        lst = sorted(sorted(S), key=lambda x: S.count(x), reverse=True)
        n = int(len(S) / 2 + 0.5)  # 奇数位数时取中间右边一位

        if lst[0] == lst[n]:  # 最多的字符超过半数
            return ''
        else:
            return ''.join(j for i in zip(lst, lst[n:]) for j in i) + ['', lst[n - 1]][len(S) % 2]

S=input()
ans=reorganizeString(S)
print(ans)