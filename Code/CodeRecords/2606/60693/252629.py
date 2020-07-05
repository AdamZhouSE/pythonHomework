nums=eval(input())
tar=int(input())
exist=False
for i in range(len(nums)):
    if nums[i]==tar:
        print(i)
        exist=True
if not exist:
    print(-1)