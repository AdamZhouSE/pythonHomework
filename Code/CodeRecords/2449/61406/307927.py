source = input().split(',')
for x in range(0,len(source)):
    source[x] = int(source[x])
target = int(input())
if source.count(target)!=0:
    print(source.index(target))
else:
    print(-1)