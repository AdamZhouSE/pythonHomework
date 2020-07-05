source = input().lstrip('[').rstrip(']').split(',')
for x in range(0,len(source)):
    source[x] = int(source[x])
source.sort()
length=1
result = 1
for x in range(0,len(source)-1):
    if source[x+1]==source[x]+1:
        length+=1
    elif source[x+1]!=source[x]:
        result = max(result,length)
        length=1
result = max(result,length)
print(result)
