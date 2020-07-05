def swap(x,y,arr):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    

def moveZero(begin,until,arr):
    while begin < until:
        swap(begin,begin+1,arr)
        begin += 1

        
def reSort(arr):
    zeroNum = 0
    i = 0
    while i < len(arr)-zeroNum-1:
        if int(arr[i]) == 0:
            zeroNum += 1
            moveZero(i,size-zeroNum,arr)
            i -= 1
        i += 1

def printArr(arr):
    i = 0
    while i < len(arr):
        print(arr[i], end="")
        if i != len(arr)-1:
            print(end=" ")
        i += 1
    print()
    
#main-----
pro = int(input())
for p in range(pro):
    size = int(input())
    arr = input().split(" ")
    
    arr[0] = int(arr[0])
    i = 0
    while i < size-1:
        arr[i+1] = int(arr[i+1])
        if arr[i] != 0 and arr[i]==arr[i+1]:
            arr[i] = 2*arr[i]
            arr[i+1] = 0
            i += 1
        i += 1
    
    reSort(arr)
    printArr(arr)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    