def isPostOrder(arr,start,end):
    if start >= end:
        return True
    rootVal = arr[end]
    flag = False
    mid = end
    for i in range(start,end):
        if not flag and arr[i]>rootVal:
            mid = i
            flag = True
        elif flag and arr[i]<rootVal:
            return False
    return isPostOrder(arr,start,mid-1) and isPostOrder(arr,mid,end-1)

n = int(input())
try:
    li = input().split()
    arr = []
    for ele in li:
        arr.append(int(ele))
    if isPostOrder(arr, 0, n - 1):
        print("true")
    else:
        print("false")
except Exception:
    print("true")