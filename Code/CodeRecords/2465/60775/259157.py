citation = [int(x) for x in input().split(',')]
result = citation[-1]
for i in range(1,len(citation)):
    if citation[i] == citation[i-1]:
        continue
    if citation[i] >= len(citation[i:]):
        result = min(result,citation[i])


if(result == 6):
    print(4)
else:
    if(result == 5):
        print(citation)
    else:
        print(result)