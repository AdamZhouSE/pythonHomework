def can_exchange(a, b):
    return sum([1 if a[t] != b[t] else 0 for t in range(len(a))]) <= 2

words = eval(input())
count = 0
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        count += 1 if can_exchange(words[i], words[j]) else 0
print(count)