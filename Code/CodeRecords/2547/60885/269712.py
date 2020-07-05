def countDif(nums, k):
    recent = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            a,b = nums[i],nums[j]
            if a > b:
                a,b = b,a
            if not (a,b) in recent and b-a == k:
                recent.append((a,b))
    return len(recent)

def test():
    N = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    return countDif(nums, k)

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)