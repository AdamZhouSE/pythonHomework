n=int(input())
player=[]
result=[]
for i in range(n):
	l=input().split(" ")
	if not (l[0] in player):
		player.append(l[0])
		result.append(int(l[1]))
	else:
		number=l.index(l[0])
		del player[number]
		player.append(l[0])
		temp=result[number]+int(l[1])
		del result[number]
		result.append(temp)
max=max(result)
winner=player[result.index(max)]
print(winner)