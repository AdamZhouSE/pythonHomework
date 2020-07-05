n = int(input())
nums = list(map(int,input().split()))
result = 0
for i in range(n):
    bl = True
    for j in range(n):
        if nums[j]%nums[i]!=0:
            bl = False
            break
    if bl:
        result=result+1
print(result)