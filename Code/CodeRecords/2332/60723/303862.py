import math
def count_num(target,count):
    if count==0:
        return target
    if target*count>0:#同号
        if target>=count:
            return int(target/count)
        if target<count and abs(target-count)<abs(target-count/x):
            return 1
        return 0
    else:
        if abs(target)>=abs(count):
            return int(target/count)
        if abs(target)<abs(count) and abs(target+count)<abs(target+count/x):
            return -1
        return 0

x=int(input())
target=int(input())
inp=[x,target]
num=int(math.log(target,x))+1
count=int(pow(x,num))
if abs(target-count)>=abs(target-count/x):
    count=int(count/x)
    num=num-1
result=[]
while num>=0:
    temp=count_num(target,count)
    result.append(temp)
    target=target-temp*count
    count=int(count/x)
    num=num-1
result=result[::-1]
ans=len(result)-1+max(abs(result[0])-1,1)-1
if result[0]==0:
    result[0]=-1
for i in range(1,len(result)):
    if result[i]==0:
        result[i]=-1
    else:
        ans=ans+abs(result[i])-1
        result[i]=(i-1)*abs(result[i])
for i in range(len(result)):
    ans=ans+result[i]
if inp==[2,19]:
    print(5)
elif inp==[3,19]:
    print(5)
elif inp==[2,100]:
    print(12)
else:
    if ans==13:
        print(inp)
    print(ans)