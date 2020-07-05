def notRepeated(nums):
    cap = []
    for num in nums:
        if num in cap:
            return False
        else:
            cap.append(num)
    return True

def test():
    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(1, N+1):
        for j in range(0, N-i+1):
            sub = nums[j:j+i]
            if notRepeated(sub):
                count += i
    A.append(count)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)