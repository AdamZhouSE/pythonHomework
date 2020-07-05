nums=list(map(int,input().split(',')))
k=int(input())
nums=sorted(nums)
print(nums[-1*k])