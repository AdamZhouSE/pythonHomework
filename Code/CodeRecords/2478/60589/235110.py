total=int(input())
results=[]
for i in range(total):
    nums=input().split()
    first=int(nums[0])
    second=int(nums[1])
    n=int(input())
    d=second-first
    result=first+d*(n-1)
    results.append(result)
for r in results:
    print(r)