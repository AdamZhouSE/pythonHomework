T = int(input())
for i in range(T):
    s = input().lower()
    t = ''
    for i in range(len(s)):
        if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
            t +=s[i]
    a = reversed(list(t))
    if list(a) == list(t):
        print('YES')
    else:
        print(' NO')