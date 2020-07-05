def func20():
    arr = list(map(int, input().split()))
    n = arr[0]
    power = arr[1:]
    position = []
    for _ in range(0, n):
        position.append(list(map(int, input().split())))
    ans = 0
    while position:
        if power[0] != position[0][0]:
            k = (power[1] - position[0][1]) / (power[0] - position[0][0])
            tem = position[:]
            for item in position:
                if power[0] != item[0] and (power[1] - item[1]) / (power[0] - item[0]) == k:
                    tem.remove(item)
            position = tem[:]
        else:
            tem = position[:]
            for item in position:
                if item[0] == power[0]:
                    tem.remove(item)
            position = tem[:]
        ans += 1
    print(ans)


func20()