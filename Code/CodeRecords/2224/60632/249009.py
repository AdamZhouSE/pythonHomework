def solve(x: list) -> list:  # 将列表中的最大值换到首位，若有多个最大值，则换最靠后的那个
    if len(x) == 1:
        return x
    else:
        copy = x[:]
        copy.reverse()
        index = len(x) - copy.index(max(x)) - 1
        maxi = max(x)
        x[index] = s[0]
        x[0] = maxi
        return x


s = list(input())
end = False
for i in range(len(s)):
    tmp = s[i:]
    if tmp[0] != max(tmp):
        s = s[:i] + solve(tmp)
        end = True
    if end:
        break
print(''.join(s))
