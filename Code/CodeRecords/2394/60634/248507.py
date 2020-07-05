def swap(x,y,arr):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    

def moveZero(begin,until,arr):
    while begin < until:
        swap(begin,begin+1,arr)
        begin += 1

pro = int(input())
for p in range(pro):
    size = int(input())
    arr = input().split(" ")
    
    zeroNum = 0
    i = 0
    while i < size-zeroNum-1:
        if int(arr[i]) == 0:
            zeroNum += 1
            moveZero(i,size-zeroNum,arr)
            i -= 1
        i += 1
        
    for x in arr:
        print(x,end=" ")
    print()