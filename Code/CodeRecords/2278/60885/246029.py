def test():
    N = int(input())
    nums = list(map(int, input().split())) + [0]
    for i in range(len(nums)-1):
        nums[i] = nums[i] ^ nums[i+1]
    result.append(' '.join(list(map(str, nums[:-1]))))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)