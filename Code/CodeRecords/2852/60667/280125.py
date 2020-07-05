n = int(input())
sushi = input().split()
s = ''.join(sushi)
max_possible = min(sushi.count('1'), sushi.count('2'))
result = 0
for window in range(max_possible, 0, -1):
    first = ''
    second = ''
    for i in range(window):
        first = first + '1'
        second = second + '2'
    if first+second in s or second+first in s:
        result = 2 * window
        break
print(result)