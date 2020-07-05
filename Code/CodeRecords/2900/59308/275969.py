s = list(input())
count = len(s)
for i in s:
    if i == ' ':
        count -= 1
print(count, end='')


