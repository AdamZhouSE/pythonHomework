def findKth(m,n,k,start,end):
    nowMid = 0
    smallN = 0
    equalN = 1
    mid = int((start+end)/2)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i * j <= mid:
                smallN = smallN + 1
                if i * j > nowMid:
                    nowMid = i * j
                    equalN = 1
                elif i * j == nowMid:
                    equalN = equalN +1
            else:
                break
    if (smallN - equalN < k) and (smallN >= k):
        return nowMid
    elif smallN < k:
        return findKth(m,n,k,mid+1,end)
    else:
        return findKth(m,n,k,start,nowMid-1)
    
m = int(input())
n = int(input())
k = int(input())
print(findKth(m,n,k,1,m*n))