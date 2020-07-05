nums=list(input())
nums=[int(x) for x in nums]
mul=1
add=0
for x in nums:
    mul*=x
    add+=x
print(mul-add)