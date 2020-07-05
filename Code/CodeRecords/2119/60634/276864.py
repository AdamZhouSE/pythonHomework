def solve(arr):
    if arr[0] < arr[2]:
        return False
    if arr[1] > arr[3]:
        return False
    return True


#main-----
arr = eval(input())
print(solve(arr))