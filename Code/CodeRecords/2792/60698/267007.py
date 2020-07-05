# 32
step = int(input())
steps = input().split()
steps = list(map(int, steps))
count = 0
res = []
i = 0
while i < len(steps):
    if steps[i] == i + 1:
        if i == len(steps) - 1:
            count = count + 1
            res.append(steps[i])
            break
        i = i + 1
    else:
        res.append(steps[i - 1])
        steps = steps[i:len(steps)]
        count = count + 1
        i = 0
res=' '.join(list(map(str,res)))
print(count)
print(res)