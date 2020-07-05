def format(s:str):
    s = s[1:len(s)-1]
    s = list(map(int,s.split(',')))
    return s
if __name__ == '__main__':
    target = int(input())
    position = format(input())
    speed = format(input())
    retv = 0
    arr = []
    length = len(position)
    for i in range(length):
        arr.append([position[i], speed[i]])
    arr = sorted(arr, key=lambda x: x[0], reverse=True)
    slowest = 0
    for i in range(length):
        if i == 0:
            slowest = (target - arr[i][0]) / arr[i][1]
            retv += 1
        elif (target - arr[i][0]) / arr[i][1] > slowest:
            retv += 1
            slowest = (target - arr[i][0]) / arr[i][1]
    print(retv)
