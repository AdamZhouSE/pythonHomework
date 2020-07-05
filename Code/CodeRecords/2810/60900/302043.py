str1 = input()
nums =[]
maxn =0
for i in range(0,len(str1)):
   nums.append(int(str1[i]))
maxn = max(nums)
result =[]
for i in range(0,len(nums)):
    if len(result)<nums[i]:
        for j in range(0, len(result)):
            result[j] += 10 ** (len(nums) - i - 1)
        for j in range(0,nums[i]-len(result)):
            result.append(10**(len(nums)-i-1))
        
    else:
        for j in range(0,nums[i]):
            result[j]+=10**(len(nums)-i-1)


print(maxn)
for i in range(0,len(result)-1):
    print(result[i],end=' ')
print(result[len(result)-1])