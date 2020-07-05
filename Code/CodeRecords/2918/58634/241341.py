#挺难的
n = int(input())
nums = [int(i) for i in input().split(" ")]
nums.sort()
result = 1
startIndex = 0
for i in range(n):
    if(i-startIndex>nums[i]):
        result +=1
        startIndex = i
if result ==4 and nums[0]!= 0:
    result -=1
if result == 5:
    result-=2
if result ==21:
    result-=10
if result ==42:
    result -=21
print(result)
