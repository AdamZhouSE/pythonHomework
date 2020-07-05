def f(nums):
    if nums[-1]==15: return "DOWN"
    if nums[-1]==0: return "UP"
    if len(nums)==1: return "-1"
    if nums[-1]-nums[-2]>0: return "UP"
    return "DOWN"
    
n=int(input())
nums=[int(x) for x in input().split()]
print(f(nums))