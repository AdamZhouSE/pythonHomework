input()
ls = list(map(int, input().split(" ")))
results = []
for i in range(1, ls.__len__()+1):
    results.append(ls.index(i)+1)
print(" ".join(str(i) for i in results))