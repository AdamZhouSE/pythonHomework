def test():
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    for i in range(1, N):
        if nums[i-1] != i:
            result.append(i)
            return
    result.append(N)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)