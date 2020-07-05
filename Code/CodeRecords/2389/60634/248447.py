def swap(x,y,arr):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def printArr(arr):
    i = 0
    while i < len(arr): 
        print(arr[i],end="")
        if i != len(arr)-1:
            print(end=" ")
        i += 1
    print()

problems = int(input())
for p in range(problems):
    size = int(input())
    array = input().split(" ")
    
    i = 0
    while i < int(size/2):
        swap(2*i,2*i+1,array)
        i += 1
    printArr(array)