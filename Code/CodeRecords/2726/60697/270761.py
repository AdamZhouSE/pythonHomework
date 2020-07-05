t=input()
lent=len(t)
t=t[1:lent-1].split(',')
nums=[]
for i in t:
    if(i!="null"):
        nums.append(int(i))
    else:
        nums.append(None)
leng=len(nums)
res=[]
def dfs(index,count):
    if(index>=leng or nums[index]==None):
        res.append(count)
        return
    dfs(2*index+1,count+1)
    dfs(2*index+2,count+1)
dfs(0,0)
print(min(res))
