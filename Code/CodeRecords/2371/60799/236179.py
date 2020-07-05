T = int(input())
for hhh in range(0, T):
    s = input()
    s = ''.join(list(filter(str.isalpha, s)))
    s = s.upper()
    if s == s[::-1]:
        print('YES')
    else:
        print('NO')