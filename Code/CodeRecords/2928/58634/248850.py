
v = int(input())
nums = [int(i) for i in input().split(" ")]
min1 = min(nums)
if(v<min1):
    print(-1)
else:
    cnt = v//min1
    while(cnt!=-1):
        for i in range(8,-1,-1):
            if (v - nums[i]) // min1 == cnt and v - nums[i] >= 0:
                print(i+1,end="")
                v = v - nums[i]
                break
        cnt-=1
    print()

