import math
def check(begin,end):
    while begin<end:
        mid=math.floor((begin+end)/2)
        if arr[mid]<=target<arr[mid+1]:
            return arr[mid+1]
        else:
            if arr[mid]<target:
                begin=mid+1
            elif arr[mid]>target:
                end=mid
    return arr[0]
    # if end==-1:
    #     return arr[0]
    # elif begin==len(arr):
    #     return arr[0]


if __name__ == '__main__':
    arr=eval(input())
    target=input()
    print(check(0,len(arr)-1))
