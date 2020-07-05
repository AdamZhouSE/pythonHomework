import collections

N = int(input())
count = collections.Counter(str(N))
for b in range(31):
    if count == collections.Counter(str(1 << b)):
        print("True")
        exit()
    else:
        continue
print("False")
