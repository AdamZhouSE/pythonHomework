def strSub(s, n, m):
    subs = ''
    for i in range(m - 1, n):
        subs += s[i]
    return subs


size = eval(input())
testStr = input()
index = eval(input())
print(strSub(testStr, size, index))