n = eval(input())
origin = list(map(int, input().split(' ')))
out = list(map(int, input().split(' ')))
count = 0
for i in range(len(origin)):
    for ori in origin[:i + 1]:
        if origin.index(ori) < i and out.index(ori) > out.index(origin[i]):
            count += 1
            break
print(count)