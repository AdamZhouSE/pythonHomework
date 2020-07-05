def insert(x,n,arr):
    i = 0
    while True:
        if i >= n:
            break
        if x > arr[i]:
            i += 1
            if i >= len(arr):
                arr.append(x)
                break
        elif x == arr[i]:
            break
        else:# x < arr[i]:
            if i >= n:
                arr.append(x)
            else:
                arr.insert(i,x)
            break
    return arr

def solve(n,arr):
    if n == 1:
        return 1
    i = 0
    while i < n:
        j = i
        while j < n:
            arr  = insert(arr[i]*arr[j],n-1,arr)
            j += 1
        i += 1
    return arr[n-2]
        


#main-----
n = int(input())
arr = input().split(',')
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(solve(n,arr))
