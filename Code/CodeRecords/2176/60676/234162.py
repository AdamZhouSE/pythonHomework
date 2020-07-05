def postfix_sort():
    string = input()
    arr = []
    for i in range(len(string)):
        arr.append(string[i:])
    arr.sort()
    res = []
    for i in range(len(arr)):
        res.append(len(string)-len(arr[i])+1)
    return res

a = postfix_sort()
for i in range(len(a)-1):
    print(a[i], end=' ')
print(a[-1])