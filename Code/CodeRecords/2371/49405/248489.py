T = int(input())
for t in range(T):
    a = input().lower()
    s = ''
    for i in range(len(a)):
        if a[i].isalpha():
            s += a[i]
    n = len(s) // 2
    if s.endswith(s[:n][::-1]):
        print('YES')
    else: print('NO')