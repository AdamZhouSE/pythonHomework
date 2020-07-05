import sys


def excute(arr,n):
    dp = [0] * (n + 1)
    dp[1] = arr[0]

    for i in range(1, n):
        dp[i + 1] = max(arr[i] + dp[i - 1], dp[i])
    print(dp[n])



Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    info = Input[begin].split()
    n = int(info[0])
    #k = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    '''
    li2 = Input[begin+2].split()
    for j in range(0,len(li2)):
        B.append(int(li2[j]))
    '''
    begin += 2
    excute(arr,n)



    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''