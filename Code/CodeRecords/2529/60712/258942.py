from collections import Counter
n = input()
print(Counter(n) in [Counter(str(1<<i)) for i in range(32)])