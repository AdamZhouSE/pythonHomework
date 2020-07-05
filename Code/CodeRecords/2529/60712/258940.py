from collections import Counter
n = input()
print(Counter(n) in [Counter(1<<i) for i in range(32)])