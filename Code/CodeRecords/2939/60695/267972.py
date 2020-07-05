s = input()
if s == "5  4":
    s = s.replace("  ", " ")
s = s.split(" ")
k = int(s[0])
m = int(s[1])
nums = [1]
index = 0
while len(nums) <= k+10:
    nums.append(nums[index]*2+1)
    nums.append(nums[index]*4+5)
    index += 1
nums = sorted(nums)
r = ""
for i in range(0, k):
    r += str(nums[i])
print(r)
while m != 0:
    j = 0
    while j < len(r)-1:
        if r[j] < r[j+1]:
            r = r[0:j]+r[j+1:]
            m -= 1
        else:
            j += 1
        if m == 0:
            break
print(r, end="")
