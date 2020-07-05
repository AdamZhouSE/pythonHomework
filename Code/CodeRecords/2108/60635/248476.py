limit=int(input())
nums=[str(n)  for n in range(1,limit+1)]
ans = 0
for num in nums:
    if '1' in num:
        ans+=num.count('1')
print(ans)
        