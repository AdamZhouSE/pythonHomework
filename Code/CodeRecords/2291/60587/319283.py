n = int(input())
nums = input().split(' ')
num = [int(nums[i]) for i in range(len(nums))]
num.sort()
num.reverse()
ans = 0
while len(num) > 1:
    a = num.pop()
    b = num.pop()
    ans = ans + a + b
    num.append(a + b)
print(ans)
