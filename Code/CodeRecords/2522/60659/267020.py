import re
list1=input()
list2=input()
pattern=re.compile(r'\d+')
arr1=pattern.findall(list1)
arr2=pattern.findall(list2)
for i in range(len(arr1)):
	arr1[i]=int(arr1[i])
for i in range(len(arr2)):
	arr2[i]=int(arr2[i])
arr3=[]
for i in arr1:
	if not(i in arr2):
		arr3.append(i)
arr3.sort()
counter=0
result=[]
while counter<len(arr2):
	for i in arr1:
		if i==arr2[counter]:
			result.append(i)
	counter+=1
for i in arr3:
	result.append(i)
print(result)