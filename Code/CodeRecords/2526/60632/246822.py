arr1 = eval(input())
arr2 = eval(input())
result = arr1 + arr2
while result.count('null') != 0:
    result.remove('null')
print(sorted(result))
