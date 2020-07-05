import collections
def sortFormat(arr1,arr2):
    s = collections.Counter(arr1)
    result = []
    for a2 in arr2:
        temp = s[a2]
        result += [a2 for _ in range(temp)]
    temp = []
    for a1 in arr1:
        if a1 not in arr2:
            temp.append(a1)
    temp = sorted(temp)
    return result + temp
print(sortFormat(eval(input()),eval(input())))