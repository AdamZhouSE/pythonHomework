init=[int(x) for x in input().split()]
n=init[0]
k=init[1]
array=[[1]*n]#表示以1……n结尾,长度为1的方案各有1种
for i in range(1,k):
    newArray=[]
    for j in range(1,n+1):
        temp=0
        for k in range(1,int(j/2)+1):
            if j%k==0:
                temp+=array[i-1][k-1]
        temp+=array[i-1][j-1]
        newArray.append(temp%1000000007)
    array.append(newArray)
print(sum(array[len(array)-1])%1000000007)