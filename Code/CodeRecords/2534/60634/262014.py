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

temp = eval(input())
arr = []
for x in temp:
    arr += x
sort(arr)
print(arr)