

info=input().split(',')
a=[int(y) for y in info]
count = collections.Counter(deck)
X = min(count.values())
for x in range(2,X+1):
    if all(v % x == 0 for v in count.values()):
        print(True)
print(False)

