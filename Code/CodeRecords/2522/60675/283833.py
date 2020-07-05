def index(li:list, string:str) -> int:
    for i in range(len(li)):
        if li[i] == string :
            return i
    return -1


def func(arr1 :list, arr2: list) -> list:
    l = []
    for i in arr2 :
        while True:
            tmp = index(arr1,i)
            if tmp != -1:
                l.append(arr1[tmp])
                arr1.remove(arr1[tmp])
            else:
                break
    arr1.sort()
    for i in arr1:
        l.append(i)
    return l
                

n = "arr1 = " + input()
m = "arr2 = " + input()
exec(n)
exec(m)
print(func(arr1,arr2))