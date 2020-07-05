def test():
    N = int(input())
    nums = list(map(int, input().split()))
    counter = {}
    for num in nums:
        if str(num) not in counter:
            counter[str(num)] = 1
        else:
            counter[str(num)] += 1
    ans = []
    for num,count in counter.items():
        if count % 2 == 1:
            ans.append(num)
    result.append(' '.join(ans))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)