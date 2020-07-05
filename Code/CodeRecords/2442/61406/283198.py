source = input().lstrip('[').rstrip(']').split(',')
for i in range(0,len(source)):
    source[i] = int(source[i])
source.sort()
maxdistance = 0
if len(source)<2:
    print(0)
else:
    for j in range(0,len(source)-1):
        if maxdistance<source[j+1]-source[j]:
            maxdistance = source[j+1]-source[j]
    print(maxdistance)
