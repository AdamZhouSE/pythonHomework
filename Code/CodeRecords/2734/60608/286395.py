
def func25():
    arr, flower = list(map(int, input().split())), list(map(int, input().split()))
    n, c, m, ops = arr[0], arr[1], arr[2], []
    for i in range(0, m):
        ops.append(list(map(int, input().split())))
    for i in range(0, m):
        res, ans, t = [], 0, ops[i]
        array = flower[t[0] - 1:t[1]]
        for j in range(0, len(array)):
            if array.count(array[j]) > 1 and array[j] not in res:
                ans += 1
                res.append(array[j])
        print(ans)


func25()