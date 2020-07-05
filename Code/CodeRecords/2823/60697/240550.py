# 给你长度为 l 的整数数列 (1 ≤ b1 ≤ b2 ≤ ... ≤ bl ≤ n)，如果每个元素都可以整除下一个元素，那么我们称这个数列是好的。
# 给你 n 和 k，请找到长度为 k 的好数列的个数吧，如果它特别大的话，请用 MOD=1000000007 取模。
#
# 输入描述
# 只有一行，为数列元素的最大值 n 和长度 k (1 ≤ n, k ≤ 2000)
# 输出描述
# 输出一个整数表示长度为 k 的好数列的个数，用 1000000007 取模
sizes=list(map(int,input().split(' ')))
n=sizes[0]
k=sizes[1]
dp=[[0 for i in range(n+1)] for j in range(k+1)]
for i in range(n+1):
    dp[1][i]=1
for i in range(1,k):
    for  j in range(1,n+1):
        tmp=int(j**0.5)
        for l in range(1,tmp+1):
            if(j%l==0):
                dp[i+1][j]=dp[i+1][j]+dp[i][l]
                if(l*l!=j):
                    dp[i+1][j]=dp[i+1][j]+dp[i][int(j/l)]
sum=0
for j in range(1,n+1):
    sum=sum+dp[k][j]
print(sum%(10**9+7))

