def foo(nums: list, k: int) -> int:
    res = []
    dic = []
    for num in nums:
        if num not in res and num not in dic:
            res.append(num)
        else:
            dic.append(num)
            if num in res:
                    res.remove(num)
    return res[k - 1] if len(res) >= k else -1

for _ in range(eval(input())):
    index = int(input().split(' ')[1])
    print(foo(list(map(int, input().split(' '))), index))