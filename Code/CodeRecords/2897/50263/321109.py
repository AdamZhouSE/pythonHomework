words = eval(input())
max_s = 0
for w1 in words:
    for w2 in words:
        if not set(w1) & set(w2):
            max_s = max(max_s, len(w1) * len(w2))
print(max_s)

