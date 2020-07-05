import bisect

def solve():
    nums=map(int,input().split(','))
    arr=[0]
    res=float('-inf')
    cur=0
    for num in nums:
        cur+=num
        bisect.insort(arr,cur)
    res=arr[len(arr)-1] if arr[0]>=0 else arr[len(arr)-1]-arr[0]
    print(res)

if  __name__ == '__main__' :
    solve()