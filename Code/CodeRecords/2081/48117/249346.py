a = input()
b = input()
a.lower()
b.lower()
bLen = len(b)
count = 0

for i in range(bLen, len(a) + 1):
    s = a[i - bLen:i]
    if s == b:
        count += 1

print(count, end='')