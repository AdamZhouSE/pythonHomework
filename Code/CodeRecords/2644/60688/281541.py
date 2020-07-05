def dfs(index:int,sum:int,k:int,begin:int):
    if(nums[index]==k):
        resultlsits.append(1);
        return 
    sum += nums[index];
    if(sum==k):
        resultlsits.append(index-begin+1);
        return
    if(index==(len(nums)-1) ):
        resultlsits.append(-1);
        return
    dfs(index+1,sum,k,begin);
nums=eval(input())
k=int(input());
resultlsits=[];
for i in range(len(nums)-1):
    dfs(i,0,k,i);
while (-1 in resultlsits):
    resultlsits.remove(-1);
result=-1;
if len(resultlsits)!=0:
    resultlsits.sort();
    result=str(resultlsits[0]);
print(result)