import re
list1=input()
list2=input()
pattern=re.compile('\-\d+|\d+')
root1=pattern.findall(list1)
root2=pattern.findall(list2)
for i in range(len(root1)):
	root1[i]=int(root1[i])
for i in range(len(root2)):
	root2[i]=int(root2[i])
result=root1+root2
result.sort()
print(result)