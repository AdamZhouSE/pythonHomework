n = int(input())
nums = input().split(' ')
num = [int(nums[i]) for i in range(len(nums))]
q = []
ans = 0
while len(num) > 1:
    a = num.pop()
    b = num.pop()
    ans = ans + a + b
    num.append(a + b)
print(ans)