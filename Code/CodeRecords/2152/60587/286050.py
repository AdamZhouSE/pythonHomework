N = int(input())
val = input().split(' ')
chan = input().split(' ')
value = [int(val[i]) for i in range(len(val))]
channel = [int(chan[i]) for i in range(len(chan))]
for i in range(0, N):
    isGet = [False] * N
    isGet[i] = True
    res = value[i]
    tmp = i
    # tmpChan = channel[i]
    # tmpVal = value[tmpChan]
    while True:
        tmpChan = channel[tmp] - 1
        tmpVal = value[tmpChan]
        if not isGet[tmpChan]:
            res += tmpVal
            isGet[tmpChan] = True
            tmp = tmpChan
        else:
            break
    print(res)
