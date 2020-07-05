source = input().lstrip('[').rstrip(']').split(',')
k = int(input())
for x in range(0,len(source)):
    source[x] = int(source[x])
source.sort()
print(source[len(source)-k])
