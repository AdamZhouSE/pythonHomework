import re
list=input()
winner="Draw"
A=[]
B=[]
pattern=re.compile("\[\d\,\d\]")
moves=pattern.findall(list)
for i in range(len(moves)):
	if i%2==0:
		A.append(moves[i])
	else:
		B.append(moves[i])
	if '[0,0]'and'[1,1]'and'[2,2]'in A:
		winner="A"
		break
	elif ('[0,0]'and'[0,1]'and'[0,2]')in A:
		winner = "A"
		break
	elif ('[0,0]'and'[1,0]'and'[2,0]')in A:
		winner = "A"
		break
	elif ('[0,2]'and'[1,1]'and'[2,0]')in A:
		winner = "A"
		break
	elif ('[1,0]'and'[1,1]'and'[1,2]')in A:
		winner = "A"
		break
	elif ('[2,0]'and'[2,1]'and'[2,2]')in A:
		winner = "A"
		break
	elif ('[0,1]'and'[1,1]'and'[2,1]')in A:
		winner = "A"
		break
	elif ('[0,2]'and'[1,2]'and'[2,2]')in A:
		winner = "A"
		break
	elif  ('[0,0]'and'[1,1]'and'[2,2]') in B:
		winner="B"
		break
	elif ('[0,0]'and'[0,1]'and'[0,2]')in B:
		winner = "B"
		break
	elif ('[0,0]'and'[1,0]'and'[2,0]')in B:
		winner = "B"
		break
	elif ('[0,2]'and'[1,1]'and'[2,0]')in B:
		winner = "B"
		break
	elif ('[1,0]'and'[1,1]'and'[1,2]')in B:
		winner = "B"
		break
	elif ('[2,0]'and'[2,1]'and'[2,2]')in B:
		winner = "B"
		break
	elif ('[0,1]'and'[1,1]'and'[2,1]')in B:
		winner = "B"
		break
	elif ('[0,2]'and'[1,2]'and'[2,2]')in B:
		winner = "B"
		break
if winner=='Draw' and len(moves)<=9:
	print("Pending")
else:
	print(winner)