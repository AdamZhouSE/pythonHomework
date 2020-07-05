import sys


def excute(arr, N, S):
    for i in range(N):
        curr_sum = arr[i]
        j = i + 1
        while j <= N:
            if curr_sum == S:
                print(i+1, end=" ")
                print(j)
                return
            if curr_sum > S or j == N:
                break
            curr_sum = curr_sum + arr[j]
            j += 1
    print(-1)


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    N = int(info[0])
    S = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    excute(arr, N, S)
