def resolve(rule):
    line = input()
    counter = [0 for i in range(len(rule))]
    ans = ''
    for c in line:
        if c in rule:
            counter[rule.index(c)] += 1
        else:
            ans += c
    for i in range(len(rule)):
        ans += rule[i] * counter[i]
    return ans

rule = input()
ans = resolve(rule)
print(ans)