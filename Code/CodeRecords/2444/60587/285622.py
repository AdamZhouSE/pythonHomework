nums, k, t = input().split(', ')
k = int(k[4:len(k)])  # nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。
t = int(t[4:len(t)])
num = nums[8:len(nums) - 1]
num = num.split(',')
num = [int(num[i]) for i in range(len(num))]
isExi = False
for i in range(0, len(num) - 1):
    for j in range(i + 1, len(num)):
        if abs(num[i] - num[j]) <= t & j - i <= k:
            
            isExi = True
            break
if isExi:
    print("true")
else:
    print("false")
