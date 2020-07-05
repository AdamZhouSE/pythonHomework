n = int(input())
k = int(input())
fact, nums = [1], ['1']
for i in range(1, n):
    fact.append(fact[i - 1] * i)
    nums.append(str(i + 1))
k -= 1
s = []
for i in range(n - 1, -1, -1):
    idx = k // fact[i]
    k -= idx * fact[i]
    s.append(nums[idx])
    del nums[idx]
print(''.join(s))