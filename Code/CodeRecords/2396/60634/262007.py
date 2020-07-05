def swap(x,y,arr):
    arr[x] = arr[x]^arr[y]
    arr[y] = arr[x]^arr[y]
    arr[x] = arr[x]^arr[y]
def over(l,r,arr):
    i = 0
    while l+i < r-i:
        swap(l+i,r-i,arr)
        i += 1
    
def solve(n,arr):
    result = []
    i = 0
    while i < len(arr):
        min = i
        j = i
        while j < len(arr):
            if arr[j] < arr[min]:
                min = j
            j += 1
        result.append(min)
        over(i,min,arr)
        i += 1
    for x in range(n):
        print(result[x]+1,end=" ")
    #print()

#main-----
n = int(input())
arr = [int(x) for x in input().split(" ")]
solve(n,arr)
