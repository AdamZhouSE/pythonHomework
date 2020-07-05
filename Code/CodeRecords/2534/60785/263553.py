listList = input().strip('[|]').split('],[')
lxy =[]
for i in listList:
    for j in i:
        lxy.append(int(j))
print(sorted(lxy))