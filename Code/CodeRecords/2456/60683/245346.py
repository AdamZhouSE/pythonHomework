src = eval(input())
sz = len(src)
counts = [0] * sz
for i in [x for x in range(sz)][::-1]:
    for j in [x for x in range(i + 1, sz)]:
        if src[i] > src[j]:
            counts[i] = counts[j] + 1
            break
print(counts)