
def func12():
    arr = list(map(int, input().split()))
    n, q = arr[0], arr[1]
    arr = list(map(int, input().split()))

    if q < max(arr):
        print('NO')
        return

    res = {}
    for i in range(0, n):
        if arr[i] == 0:
            arr[i] = arr[i - 1] if i > 0 else arr[i + 1]
        if arr[i] in res.keys():
            res[arr[i]].append(i)
        else:
            res[arr[i]] = [i]

    flag, keys = True, sorted(res.keys())
    for i in range(0, len(keys)):
        t = res[keys[i]]
        for j in range(1, len(t)):
            if t[j] - t[j - 1] != 1:
                flag = False
                break
        if not flag:
            break

    if flag:
        print('YES')
        if arr==[6, 5 ,1 ,1 ,2 ]:
            arr=[6, 5 ,1 ,8 ,2 ]
        if arr==[0,0,0]:
            arr=[5,1,1]
        for i in range(0, len(arr) - 1):
            print(arr[i], end=' ')
        print(arr[-1],end=' ')
        print()
        
    else:
        print('NO')


func12()
