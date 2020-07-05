a=(input()[1:-1]).split(',')
resultList=[]
for i in a:
	resultList.append(int(i))
sorted(resultList)
print(resultList)
