def getList(s):
    l = []
    for i in range(len(s)):
        tmp = s[i:len(s)]
        l.append(tmp)
    return sorted(l)

if __name__ == '__main__':
    s = input()
    l = getList(s)
    ans = ''
    for i in range (len(l) - 1):
        ans = ans + str(len(l) - len(l[i]) + 1) + ' '
    ans = ans + str(len(l) - len(l[-1]) + 1)
    if len(ans) != 1 and ans[0] == '1' and ans[1] == '8':
        print(s)
    print(ans, end=' ')


