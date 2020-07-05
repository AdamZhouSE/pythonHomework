def subsequence(nums,lower,upper,list,out):
    if(sum(nums)>=lower and sum(nums)<=upper and list.count(nums)==0):
        out+=1
        list.append(nums)
    if(len(nums)>1):
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            out=subsequence(temp,lower,upper,list,out)
    return out

nums = eval(input())
lower = int(input())
upper = int(input())
nums.sort()
list = []
out = subsequence(nums,lower,upper,list,0)
print(out)