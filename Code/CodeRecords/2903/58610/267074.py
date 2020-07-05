dp = [set()]
res = 0
for s in eval(input()):
    set_s = set(s)
    if len(set_s) != len(s):
        continue
    for jigsaw_s in dp:
        if jigsaw_s & set_s:
            continue
        dp.append(jigsaw_s | set_s)
        res = max(res, len(dp[-1]))
print(res)