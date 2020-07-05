source = input().split(',')
target = int(input())
for a in range(0,len(source)):
    source[a] = int(source[a])
if source.count(target)!=0:
    print(source.index(target))
else:
    source.append(target)
    source.sort()
    print(source.index(target))
    