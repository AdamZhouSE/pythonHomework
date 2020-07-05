def qucikSort(start,end):
    left=start
    right=end
    basis=arr[left]
    while left<right:
        while left<right and arr[right]>=basis:
            right-=1
        arr[left]=arr[right]
        while left<right and arr[left]<basis:
            left+=1
        arr[right]=arr[left]
    arr[left]=basis
    return left

def find(start,end,k):
    if start==end:
        return
    else:
        if start<end:
            num=qucikSort(start,end)
        if num==k:
            return
        elif num>k:
            find(start,num-1,k)
        else:
            find(num+1,end,k)

if __name__ == '__main__':
    t=int(input())
    for i in range(0,t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        find(0,n-1,k)
        print(arr[k-1])