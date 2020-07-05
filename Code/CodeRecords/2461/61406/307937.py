source = input().split(',')
for a in range(0,len(source)):
    source[a] = int(source[a])
print(min(source))