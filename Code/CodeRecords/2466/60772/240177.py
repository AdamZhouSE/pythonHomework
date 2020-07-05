import sys

def findnumberofTriangles(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(0, n - 2):
        k = i + 2
        for j in range(i + 1, n):
            while (k < n and arr[i] + arr[j] > arr[k]):
                k += 1
            if (k > j):
                count += k - j - 1
    return count


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    arr = []
    li = Input[begin+1].split()
    for j in range(0,len(li)):
        arr.append(int(li[j]))
    print(findnumberofTriangles(arr))
    begin += 2
