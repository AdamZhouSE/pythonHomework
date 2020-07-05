a = list(eval(input()))
b = []
for i in a:
    for j in i:
        b.append(j)
print(sorted(b))