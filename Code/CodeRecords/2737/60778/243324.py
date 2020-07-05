str=input()
nums=list(map(int,str[1:len(str)-1].split(",")))
len=len(nums)
countA=0
countB=0
for(i=0;i<len;i++):
    if(countA==0||a==nums[i]):
        a=nums[i]
        countA++
    else if(countB==0||b==nums[i]):
        b=nums[i]
        countB++
    else:
        countA--
        countB--
countA=0
countB=0
for(i=0;i<len;i++):
    if(nums[i]==a)countA++
    if(nums[i]==b)countB++
if(countA>len/3&&countB>len/3)print([a,b])
else if(countA>len/3)print([a])
else print([b])
        