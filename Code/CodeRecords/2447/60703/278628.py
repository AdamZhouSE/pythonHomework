m,n = [int(x) for x in input().split(" ")]
nums= [int(x) for x in input().split(" ")]
res = []
for i in range(n):
    start,end = [int(x) for x in input().split(" ")]
    res.append(min(nums[start-1:end]))
print(" ".join([str(x) for x in res]),end=" ")