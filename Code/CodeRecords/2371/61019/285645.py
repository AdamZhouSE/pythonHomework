t = eval(input())
for _ in range(t):
    s = input().upper()
    s = [x for x in s if x.isalnum()]
    s = ''.join(s)
    print('YES' if s == s[::-1] else 'NO')
