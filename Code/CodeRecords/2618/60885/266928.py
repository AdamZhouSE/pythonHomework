def test():
    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
                break
    if count >= N/2:
        count = N-count
    A.append(count)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)