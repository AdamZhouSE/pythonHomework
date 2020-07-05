citation = input().split(',')
citation = [int(x) for x in citation]
h = -1
for i in range(len(citation)):
    if len(citation) - i >= citation[i]:
        h = citation[i]
print(h)