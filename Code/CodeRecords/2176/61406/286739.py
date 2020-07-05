source1 = input()
source = list(source1)
source.sort()
sa = []
for i in source:
    index = source1.rfind(i)
    sa.append(index+1)
    source1 = source1[0:index]+'/'+source1[index+1:]
result = ""
for x in sa:
    result = result+str(x)+" "
print(result.rstrip(' '))