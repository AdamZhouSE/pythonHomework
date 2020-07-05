k, n = input().split(",")
k = int(k)
n = int(n)

res=[]
def helper(count,i,tmp,target):
    if(count==k):
        if(target==0):
            res.append(tmp)
        return
    for j in range(i,10):
        if(j>target):
            break
        helper(count+1,j+1,tmp+[j],target-j)
helper(0,1,[],n)
print(res)


 