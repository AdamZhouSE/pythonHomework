inp = input()
tmp = inp[1:len(inp) - 1]
arr1 = tmp.split(',')
inp = input()
tmp = inp[1:len(inp) - 1]
arr2 = tmp.split(',')
arr2.sort()
isHas = [False] * len(arr2)
for i in range(0, len(arr1)):
    for j in range(0, len(arr2)):
        if (arr1[i] == arr2[j]) & (not isHas[j]):
            isHas[j] = True
            break
res = '['
for i in range(0, len(arr2)):
    if isHas[i]:
        res += str(arr2[i]) + ', '
res = res[0:len(res) - 2]
res += ']'
print(res)