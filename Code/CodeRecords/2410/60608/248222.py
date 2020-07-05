def func13():
    nums = eval(input())
    diff = eval(input())
    res = {}
    for item in nums:
        res[item] = res[item - diff] + 1 if item - diff in res else 1
    print(max(res.values()))


func13()
