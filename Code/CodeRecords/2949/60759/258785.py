lst = input().split()
lst.pop()
ans = ''
for i in reversed(lst):
    ans += i + ' '
print(ans, end='')
