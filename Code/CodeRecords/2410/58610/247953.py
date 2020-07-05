a: list = eval(input())
diff: int = eval(input())
res = {}
for num in a:
    res[num] = res[num - diff] + 1 if num - diff in res else 1
print(max(res.values()))