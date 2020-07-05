num_test = int(input())
ans = []
for i in range(0, num_test):
    n = int(input())
    nums = [int(x) for x in input().split()]
    odd = []
    even = []
    for j in nums:
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    even.sort()
    odd.sort()
    odd.reverse()
    odd.extend(even)
    ans.append(odd)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
