n=int(input())
nums=list(map(int,input().split(" ")))
number=0
nums.sort()

while (number<n-3):
    nums[-1]=nums[-1]-nums[number]
    nums[number]=0
    number+=1
    nums.sort()
if nums[-1]-nums[-2]>nums[-3] or (nums[-3]-nums[-1]+nums[-2])%2!=0:
    print("NO")
else:
    print("YES")