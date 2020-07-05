n = int(input())
nums = list(map(int, input().split()))
m = int(input())
for i in range(m):
    temp = list(input().split())
    if temp[0] == 'add':
        nums.append(int(temp[1]))
        nums.sort()
        n += 1
    else:    
        print(nums[int((n-1)/2)])