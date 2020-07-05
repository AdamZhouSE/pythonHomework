source=input().lstrip('[').rstrip(']').split(',')
for x in range(0,len(source)):
    source[x]=int(source[x])
source.sort()
print([int(x) for x in source])