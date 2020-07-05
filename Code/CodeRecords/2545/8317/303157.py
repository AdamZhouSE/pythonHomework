def solve():
    num = int(input())

    for _ in range(num):
        arr = [int(i) for i in input().split(' ')]
        calc(arr)


def calc(arr):
    arr.sort()
    pos = -1

    if(0 in arr):
        print('Yes')
        return

    for i in range(len(arr)):
        if(i < len(arr)-1 and arr[i] < 0 and arr[i+1] > 0):
            pos = i

    if(pos == -1):
        print('No')
        return

    sPos = ePos = pos
    add = arr[pos]

    while(sPos >= 0 and ePos < len(arr)):
        if(add < 0):
            ePos += 1
            if(ePos == len(arr)):
                print('No')
                return
            add = add + arr[ePos]
        elif(add < 0):
            sPos -= 1
            if(sPos == -1):
                print('No')
                return
            add = add + arr[sPos]
        else:
            print('Yes')
            return

solve()
