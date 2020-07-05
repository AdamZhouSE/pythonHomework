num=int(input())
nums=list(map(int,input().split(" ")))
nums.sort()
for i in range(0,num-2):
    if nums[i]+nums[i+1]>nums[i+2]:
        print("YES")
        break
    elif i==num-3:
        print("NO")
    else:
        continue