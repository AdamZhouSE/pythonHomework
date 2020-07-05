def maxStrLen(arr):
    resarr=['']
    for x in arr:
        if len(set(x))!=len(x):
            continue
        length=len(resarr)
        for i in range(length):
            if not set(x)&set(''.join(resarr[i])):
                resarr.append(x+resarr[i])

    return max(len(str) for str in resarr)

arr=eval(input())
print(maxStrLen(arr))