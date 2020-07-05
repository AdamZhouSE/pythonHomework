N,S  = [int(x) for x in input().split(" ")]
nums = []
for i in range(N):
    nums.append(int(input()))
for i in range(N):
    maxx = 0
    thisNums = nums[i:]
    for j in range(i,i+(N-i)//2):
        sum1 = sum(nums[i:j+1])
        sum2  =sum(nums[j+1:j+1+j+1-i])
        if(sum1<=S and sum2<=S):
            maxx = j-i+1
    print(maxx*2)