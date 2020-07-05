citation = [int(x) for x in input().split(',')]
h = 0
for i in range(len(citation)):
    if citation[i] <= len(citation)-i:
        h = max(h,citation[i])
print(h)
