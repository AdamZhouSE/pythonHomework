k, m = list(map(int, input().split(' ')))
s = list(input())
for _ in range(eval(input())):
    a, b, c = list(map(int, input().split(' ')))
    s[c:c] = s[a:b]
    s = s[:m]
print(''.join(s[:k]), end='')