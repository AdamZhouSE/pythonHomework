def solve(l, sum) -> int:
    sum = int(sum)
    count = 1
    res = []
    for i in l:
        if i == "1":
            res.append(count)
            count = 1
        else:
            count += 1
    res.append(count)
    all = 0
    for i in range(len(res) - sum):
        all += res[i] * res[i + sum]
    return all

num = int(input())
for j in range(num):
    arr, n = input().split()
    arr = list(arr)
    print(solve(arr, n))