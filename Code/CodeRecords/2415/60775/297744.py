

num_v = int(input())
value = [int(x) for x in input().split(' ')]
value.insert(0,1)

dp = []
for i in range(num_v+1):
    dp.append([1]*(num_v+1))
pre = []
for i in range(num_v+1):
    pre.append([1]*(num_v+1))

for leng in range(1,num_v+1):
    for l in range(1,num_v-leng+2):
        r = l+leng-1
        if l == r:#叶节点
            dp[l][r] = value[l]
            pre[l][r] = l
        else:
            for k in range(l,r+1):
                left = 1
                right = 1
                if k!=l:
                    left = dp[l][k-1]
                if k!=r:
                    right = dp[k+1][r]
                if dp[l][r] < left * right + value[k]:
                    dp[l][r] = left*right + value[k]
                    pre[l][r] = k
print(dp[1][num_v])
result = []
def prefix(l,r):
    if l <= r:
        x = pre[l][r]
        result.append(x)
        prefix(l,x-1)
        prefix(x+1,r)
prefix(1,num_v)
print(' '.join(str(x) for x in result),end =' ')
