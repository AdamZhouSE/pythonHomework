n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i]= int(nums[i])
k =int(input())
targets = input().split(' ')
for i in range(0,k):
    targets[i]= int(targets[i])

for i in range(0,k):
    count =0
    j=0
    while count<targets[i]:
        count+=nums[j]
        j+=1
    print(j)