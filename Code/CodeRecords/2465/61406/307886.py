source = input().split(',')
for a in range(0,len(source)):
    source[a] = int(source[a])
source.reverse()
for h in range(0,len(source)):
    if source[h]<=h+1:
        print(source[h])
        break
