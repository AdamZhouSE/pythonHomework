n_m = input()
a = input()
a_new = a.split()
b = input()
b_new = b.split()
counts = []
for i in b_new:
    count = 0
    for q in a_new:
        if int(i) >= int(q):
            count += 1
    counts.append(count)
print(' '.join(str(i) for i in counts))

