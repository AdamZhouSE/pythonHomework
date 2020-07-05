string=input()
type=[]
num=[]
for i in string:
	if not(i in type):
		type.append(i)
		num.append(1)
	else:
		num[type.index(i)]+=1

res=True
for i in num:
	if 2*i>len(string)+1:
		res=False
		break

if res:
	result = ''
	counter = 0
	while len(result) < len(string):
		if num[counter] > 0:
			result += type[counter]
			num[counter] -= 1
		else:
			del type[counter]
			del num[counter]
		counter += 1
		if counter >= len(type):
			counter = 0
	print(result)

else:
	print('')