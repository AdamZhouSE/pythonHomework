List = input().strip('[|]').split('],[')
pairs = [[int(i) for i in element.split(",")] for element in List]
lxy =[]
for i in pairs:
    for j in i:
        lxy.append(j)
print(sorted(lxy))