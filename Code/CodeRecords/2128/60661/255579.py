a=eval(input())
res=0;rec=0
nums=[]
length=len(a)
for i in range(length):
    nums.append(i)
    res+=a[i]*nums[i]
rec=res
for i in range(1,length+1):
    temp=rec-nums[length-1]*a[length-i]
    temps=list(a);temps.remove(a[length-i])
    temp+=sum(temps)
    res=max(res,temp)
    rec=temp
print(res)