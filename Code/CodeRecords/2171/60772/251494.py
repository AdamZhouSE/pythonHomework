import sys

def execute(arr,N):
    even = []
    odd = []
    for ele in arr:
        if ele % 2 == 0:
            even.append(ele)
        else:
            odd.append(ele)
    res = even + odd
    for m in range(0, N):
        print(res[m], end=" ")
    print("")

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

    begin += 2

    #print(execute(arr,N))
    execute(arr,N)
