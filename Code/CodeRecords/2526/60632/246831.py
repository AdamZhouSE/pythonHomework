arr1 = list(map(str, input()[1:-1].split(',')))
arr2 = list(map(str, input()[1:-1].split(',')))
result = arr1 + arr2
while result.count('null') != 0:
    result.remove('null')
result = [int(x) for x in result]
print(sorted(result))
