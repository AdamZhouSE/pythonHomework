chips=eval(input())
res = [0, 0]
for c in chips:
    res[c % 2] += 1
print(min(res))
