n = int(input())
nums = set([int(i) for i in input().split(" ")])
if(len(nums)<=3):
    print("YES")
else:
    print("NO")

