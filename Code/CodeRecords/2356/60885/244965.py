def isMid(mid, left, right):
    for num in left:
        if num > mid:
            return False
    for num in right:
        if num < mid:
            return False
    return True

def test():
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(1,len(nums)-1):
        mid = nums[i]
        if isMid(mid, nums[:i], nums[i+1:]):
            result.append(mid)
            break
    else:
        result.append(-1)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)