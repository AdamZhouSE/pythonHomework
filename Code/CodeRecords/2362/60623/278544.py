num=int(input())
result = 0
l=[]
w=[]
i = num
while i>=1:
	l.append(i)
	i-=1
i = 0
s = ""
if (num == 1):
	print(1)
else:
	while (i < len(l)):
		if (i == len(l) - 1) :
			break
		if (i % 4 == 0) :
			x = l[i]
			y = l[i + 1]
			temp = x * y
			l[i + 1] = temp
			if (i + 1 == len(l) - 1) :
				w.append(temp)


		elif (i % 4 == 1) :
			x = l[i]
			y = l[i + 1]
			temp = x // y
			l[i + 1] = temp
			if (i + 1 == len(l) - 1):
				w.append(temp)
		elif (i % 4 == 2):
			w.append(l[i])
			w.append(l[i + 1])
		else :
			if (i + 1 == len(l) - 1):
				w.append(l[i+1])
		i+=1

	k = 0
	result = w[0]
	while (k < len(w)) :
		if (k == len(w) - 1) :
			break

		else:
			if (k % 2 == 0):
				result += w[k + 1]

			else :
				result -= w[k + 1]


		k+=1

	print(result)
