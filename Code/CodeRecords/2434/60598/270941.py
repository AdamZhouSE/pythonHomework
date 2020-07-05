line1 = input().split(" ")
n = int(line1[0])
m = int(line1[1])
c = int(line1[2])
nums = list(map(int, input().split(" ")))
finish = False
for i in range(len(nums) - m + 1):
    temp = sorted(nums[i:i+m])
    if temp[-1] - temp[0] <= c:
        finish = True
        print(i+1)
if not finish:
    print("NONE",end = "")
