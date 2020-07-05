n = int(input())
list1 = []
i = 0
try:
    while True:
        inp = input()
        list1.append(inp)
except EOFError:
    pass
result = 'YES'
str1 = ''
for i in range(n-1):
	if(list1[i][i] != list1[i][n-i-1] or list1[i+1][i+1] != list1[i][i]):
		result = 'NO'
		break
if(list1[0][0] != list1[n-1][0]):
	result = 'NO'
if(result == 'NO'):
	print('NO')
else:
	char = list1[0][0]
	for i in range(n):
		list1[i] = list1[i].replace(char,'')
	for i in range(n):
		str1 += list1[i]
	for i in range(len(str1)-1):
		if(str1[i] != str1[i+1]):
			result = 'NO'
	
	print(result)

