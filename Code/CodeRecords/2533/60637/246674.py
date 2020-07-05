nums=input().replace('[','').replace(']','').split(',')
result='['
for i in range(0,len(nums)):
    if((int)(nums[i])%2==0):
        result+=nums[i]+', '
for i in range(0, len(nums)):
    if ((int)(nums[i])%2!=0):
        result+=nums[i]+', '
print(result[0:len(result)-2]+']')






