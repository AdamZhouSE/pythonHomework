def test():
    N = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                temp = nums[i]*nums[j]*nums[k]
                if temp > ans:
                    ans = temp
    result.append(ans)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)