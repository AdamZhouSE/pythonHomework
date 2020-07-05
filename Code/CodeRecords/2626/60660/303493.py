def getmaxcoins(i,j,num,memo):
    if i==j-1:
        return 0
    if memo[i][j]>0:
        return memo[i][j]
    else:
        temp=0
        for k in range(i+1,j):
            left=getmaxcoins(i,k,num,memo)
            right=getmaxcoins(k,j,num,memo)
            temp=max(temp,left+right+num[i]*num[j]*num[k])
        memo[i][j]=temp
        return memo[i][j]
num=eval('['+input()+']')
num.append(1)
num.insert(0,1)
memo=[[0 for _ in range(len(num))] for _ in range(len(num))]
print(getmaxcoins(0,len(num)-1,num,memo))