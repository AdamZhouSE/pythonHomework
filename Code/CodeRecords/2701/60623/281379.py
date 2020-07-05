def win(l):
	w=""
	if l[0][0]==l[0][1] and l[0][1]==l[0][2]:
		w=l[0][0]
	elif l[1][0]==l[1][1] and l[1][1]==l[1][2]:
		w=l[1][0]
	elif l[2][0]==l[2][1] and l[2][1]==l[2][2]:
		w=l[2][0]
	elif l[0][0]==l[1][0] and l[1][0]==l[2][0]:
		w=l[0][0]
	elif l[0][1]==l[1][1] and l[1][1]==l[2][1]:
		w=l[0][1]
	elif l[0][2]==l[1][2] and l[1][2]==l[2][2]:
		w=l[0][2]
	elif l[0][0]==l[1][1] and l[1][1]==l[2][2]:
		w=l[0][0]
	elif l[0][2]==l[1][1] and l[1][1]==l[2][0]:
		w=l[0][2]
	return w


temp=eval(input())
l=[]
for i in range(3):
	tempList=[]
	for j in range(3):
		tempList.append(" ")
	l.append(tempList)
i=0
t=0
while i<len(temp):
	a=temp[i][0]
	b=temp[i][1]
	if i%2==0:
		l[a][b]='X'
	else:
		l[a][b]='O'
	if win(l)=='X':
		t=1
		print('A')
		break
	elif win(l)=='O':
		t=1
		print('B')
		break
	else:
		i+=1
j=0
signal=0
if t==0:
	while j<len(l):
		k=0
		while k<len(l[j]):
			if l[j][k]==' ' and signal==0:
				print('Pending')
				signal=1
				break
			k+=1
		j+=1
	if signal==0:
		print('Draw')