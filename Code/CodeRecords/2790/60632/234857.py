n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
result = ''
for j in b:
    count = 0
    for i in a:
        if i <= j:
            count += 1
    result = result + str(count) + ' '
print(result[:-1])