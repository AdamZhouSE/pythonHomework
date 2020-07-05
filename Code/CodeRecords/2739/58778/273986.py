s=input()
sl=s.split(', ')
k=int(sl[0])
n=int(sl[1])
def combinationSum(k:int,n:int):
    res=[]
    def helper(count,i,tmp,target):
        #count：当前已经使用的数字,i：当前访问的数字,tmp：中间结果,target：下一步的目标和
        #print(count,i,tmp,target)
        if(count==k):
            if(target==0):
                res.append(tmp)
            return
        for j in range(i,10):
            if(j>target):
                break
            helper(count+1,j+1,tmp+[j],target-j)
    helper(0,1,[],n)
    return res
print(combinationSum(k,n))