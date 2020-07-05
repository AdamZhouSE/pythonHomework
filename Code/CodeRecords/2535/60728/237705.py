import operator


def f(s):
    leng = len(s)
    for i in range(0, leng):
        s[i] = int(s[i])

    return s


def solution(arr):
    i = 0
    j = 0
    res = 0
    length=len(arr)
    while i<length:
        if arr[i] == i:
            res=res+1
            i=i+1
            continue;
        max=arr[i]
        j=i
        while j<length:
            j=j+1
            if max<arr[j]:
                res=res+1
                i=j
                break
            if j==length-1:
                res=res+1
                i=length
                break
            if max>arr[j]:
                continue

    return res


a = input()
a = list(a)
a[0] = ''
a[len(a) - 1] = ''
s = ''.join(a)
m = s.split(",")
m = f(m)
print(solution(m))
