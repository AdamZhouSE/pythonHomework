n = int(input())
k = int(input())
strs=[]
nums =[]
for i in range(1,n+1):
    nums.append(i)


def rank(nums, bb):
    if len(nums)==1:
        bb+=str(nums[0])
        strs.append(bb)
        return
    else:
        for i in range(0,len(nums)):
            ab =bb
            temp =[]
            for j in range(0,len(nums)):
                temp.append(nums[j])

            ab+=str(nums[i])
            del temp[i]
            rank(temp,ab)
        return

aa =""

rank(nums,aa)

print(strs[k-1])