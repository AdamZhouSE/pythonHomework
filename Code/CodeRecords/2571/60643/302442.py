def findMaxSum(arr,k):#查找小于k的最大sum值
    maxSum=arr[0]
    rollerSum=arr[0]
    for i in range(1,len(arr)):
        if rollerSum>0:
            rollerSum += arr[i]
        else:
            rollerSum=arr[i]
        maxSum = max(maxSum,rollerSum)
    if maxSum<=k:
        return maxSum
    else:
        maxSum=float('-inf')
        for i in range(len(arr)):
            tmp=0
            for j in range(i,len(arr)):
                tmp+=arr[j]
                if tmp<=k and maxSum<=tmp:
                    maxSum=tmp
                if maxSum==k:
                    return k
        return maxSum


def solution(mat,k):
    row=len(mat)
    col=len(mat[0])
    maxSum=float('-inf')#Python中的最小值表示
    for l in range(col):
        rollerSum=[0]*row
        for r in range(l,col):
            for i in range(row):
                rollerSum[i]+=mat[i][r]
            maxSum=max(maxSum,findMaxSum(rollerSum,k))
            if maxSum==k:
                return k
    return maxSum


if __name__=="__main__":
    n=int(input())
    mat=[]
    for _ in range(n):
        tmp=list(map(int,input().split(",")))
        mat.append(tmp)
    k=int(input())
    ans=solution(mat,k)
    print(ans)