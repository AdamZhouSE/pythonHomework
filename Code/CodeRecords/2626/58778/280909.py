n=eval(input())
def func(lis):
    if not lis:
        return 0
    #选择最后戳的气球，该气球不在边界上
    def getMax(lis,i,j):
        if i==j-1:
            return 0
        temp=0
        
        for k in range(i+1,j):
            left=getMax(lis,i,k)
            right=getMax(lis,k,j)
            #ij为边界且不可能最后被戳破（都为1），最后只会剩2个
            temp=max(temp,left+right+lis[i]*lis[k]*lis[j])
        return temp
    lis=[1,*lis,1]
    return getMax(lis,0,len(lis)-1)
print(func(n))