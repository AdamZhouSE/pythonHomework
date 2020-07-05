n=int(input())
if n>0:
    arr=[int(x) for x in input().split()]
def judge(l,r):
    if l>=r:
        return True
    index=l
    while arr[index]<arr[r]:
        index+=1
    for i in range(index,r):
        if arr[i]<arr[r]:
            return False
    if index==l or index==r:
        return judge(l,r-1)
    return judge(l,index-1) and judge(index,r-1)
print('true' if judge(0,n-1) else 'false')