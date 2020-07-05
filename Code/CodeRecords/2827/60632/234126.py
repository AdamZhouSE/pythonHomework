n = input()
cubes = sorted(list(map(int, input().split(' '))))
result = ''
for i in cubes:
    result = result + str(i) + ' '
print(result[:-1])