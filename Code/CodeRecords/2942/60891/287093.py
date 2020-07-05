n = int(input())
s = input().split()
s.sort(reverse=True)
for i in range(n):
    print(s[i], end='')
print()