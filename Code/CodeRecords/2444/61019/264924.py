a = input().split(' ')
nums = eval(a[2][:-1])
k = eval(a[5][:-1])
t = eval(a[8])
for i in range(len(nums) - k):
    for j in range(1,k+1):
        if abs(nums[i] - nums[i+j]) <= t:
            print('true')
            exit()
print('false')