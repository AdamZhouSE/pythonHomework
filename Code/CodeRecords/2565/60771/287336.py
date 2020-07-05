#19
nums1 = eval("["+input()+"]")
nums2 = eval("["+input()+"]")

for i in nums2:
    nums1.append(i)

nums1.sort()
outcome = 0.0
n = len(nums1)//2
if len(nums1) % 2 == 1:
    outcome = nums1[n]
else:
    outcome = (nums1[n] + nums1[n-1])/2

print(format(outcome,".5f"))