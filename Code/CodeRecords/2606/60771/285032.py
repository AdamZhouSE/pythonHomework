#03
def binary(arr,l,r,x):
    if r > l:
        mid = int(l + (r-1)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary(arr,l,mid-1,x)
        else:
            return binary(arr,mid+1,r,x)
    else:
        return -1
num = eval(input())
n = int(input())
outcome = binary(num,0,len(num)-1,n)
print(outcome)
