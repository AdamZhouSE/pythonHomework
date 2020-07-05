def test():
    N = int(input())
    nums = list(map(int, input().split()))
    X = int(input())
    count = 0
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-2):
            for k in range(j+1, len(nums)-1):
                for l in range(k+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == X:
                        result.append(1)
                        return
    result.append(0)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)