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
# [5,1,4,null,null,3,6]
def helper(index):
    if(index>=leng or nums[index]==None):
        return True
    if(index*2+1<leng and nums[index*2+1]>nums[index]):
       return False
    if(index*2+2<leng and nums[index*2+2]<nums[index]):
        return False
    return helper(index*2+1) and helper(index*2+2)
flag=helper(0)
if(flag):
    print("true")
else:
    print("false")