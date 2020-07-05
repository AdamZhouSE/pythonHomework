n = input()
cubes = sorted(list(input().split(' ')))
result = ''
for i in cubes:
    result = result + i + ' '
print(result[:-1])