import sys

def execute(arr, n, k):
    max,min,count = 0,0,0
    for i in range(0,n):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]

    mark = [0]*(max+1)
    for i in range(0,n):
        mark[arr[i]] += 1
        
    for i in range(min,max+1):
        if mark[i] >= 1:
            for j in range(i,max+1):
                if mark[j] >= 1:
                    if j == i and mark[i] == 1:
                        continue
                currentDiff = abs(j - i)
                if currentDiff == k:
                    count += 1

    return count


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

    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))

    k = int(Input[begin + 2])
    begin += 3

    print(execute(arr, N, k))
    # execute(s,len(s))
