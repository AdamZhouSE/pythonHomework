def greatest(n):
    nums = [int(i) for i in str(n)]
    nums.sort()
    return int(''.join(str(i) for i in nums)[::-1])

n = int(input())
nums = greatest(n)
i=1
out = False
while (i<=nums):
    if(greatest(i)==nums):
        out = True
        break
    i=i*2
print(out)