n = input()
types = set(input().split(' '))
count = 0
for x in types:
    if x != '0':
        count += 1
print(count)