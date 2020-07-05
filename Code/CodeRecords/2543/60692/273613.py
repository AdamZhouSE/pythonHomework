nums = int(input())
res = []
for j in range(nums):
    list1 = []
    ans = []
    n = int(input())
    a = input().split(" ")
    a = [int(i) for i in a]
    for i in range(1, n + 1):
        for k in range(0, n - i + 1):
            ans.append(min(a[k:k + i]))
        list1.append(max(ans[0:]))
        ans.clear()
    list1 = [str(m) for m in list1]
    res.append(" ".join(list1))
for n in res:
    print(n)