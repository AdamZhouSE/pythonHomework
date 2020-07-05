n=int(input())
nums=input().split(" ")
nums=list(int(a) for a in nums)
maxlen=1
len=1
for i in range(1,n):
    if(nums[i]>nums[i-1]):
        len=len+1
    else:
        if(len>maxlen):
            maxlen=len
        len=1
if(len>maxlen):
    maxlen=len
print(maxlen)
   