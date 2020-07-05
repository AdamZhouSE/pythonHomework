a = set(eval(input()))
b = set(eval(input()))
for i in b.difference(a):
    b.remove(i)
print(sorted(b))

