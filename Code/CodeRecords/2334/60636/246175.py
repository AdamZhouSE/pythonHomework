from itertools import combinations
lists=input().split(",")
sources=[]
for i in lists:
    sources.append(int(i))
target=lists(combinations(sources,3))

