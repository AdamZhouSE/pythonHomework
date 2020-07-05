def winner(n,i):
	i=i+1
	if n<4:
		if i%2==0:
			return True
		else:
			return False
	else:
		return winner(n-1,i) or winner(n-2,i) or winner(n-3,i)

n=int(input())
print(winner(n,1))