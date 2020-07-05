def bOrS(order, x, y):
    if order == 0:
        return y < x
    else:
        return x < y
def filter(order, l, r, arr):
    while r > l:
        if bOrS(order, int(arr[r-1]), int(arr[r])):
            temp = arr[r-1]
            arr[r-1] = arr[r]
            arr[r] = temp
        r -= 1
def sortS(order, l, r, arr):
    i = l + 1
    while i <= r:
        filter(order, l, i, arr)
        i += 1
def sort(arr):
    sortS(0,0,len(arr)-1,arr)

def solve(arr1,arr2):
    curr = -1
    result = []
    i = 0
    while i < len(arr1):
        if arr1[i] != curr:
            j = 0
            while j < len(arr2):
                if arr2[j] != curr:
                    if arr1[i] == arr2[j]:
                        curr = arr1[i]
                        result.append(curr)
                        break
                j += 1
        i += 1
    print(result)
            
#main-----
arr1 = eval(input())
arr2 = eval(input())
sort(arr1)
sort(arr2)
solve(arr1,arr2)
