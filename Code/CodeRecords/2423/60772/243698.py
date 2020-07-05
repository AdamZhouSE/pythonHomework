import sys


def excute(arr1,arr2, m,n):
    count = 0
    for i in range(0,n):
        if arr2[i] in arr1:
            count += 1
    if count == n:
        print("Yes")
    else:
        print("No")


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    m = int(info[0])
    n = int(info[1])
    arr1 = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr1.append(int(li[j]))

    arr2 = []
    li2 = Input[begin+2].split()
    for j in range(0,len(li2)):
        arr2.append(int(li2[j]))
    begin += 3
    excute(arr1,arr2,m,n)