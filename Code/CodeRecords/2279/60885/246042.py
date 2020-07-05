def test():
    N,S = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            total = 0
            for num in nums[i:j]:
                total += num
            if total == S:
                result.append('%d %d'%(i+1,j))
                return
    result.append(-1)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)