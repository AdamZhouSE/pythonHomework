num = int(input())
douc = int(input())
U = []
try:
    while True:
        inp = int(input())
        U.append(inp)
except EOFError:
    pass
m = num-1
while( m >= 0):
	for n in range(m):
		if(U[n] < U[n+1]):
			temp = U[n+1]
			U[n+1] = U[n]
			U[n] = temp
	m -=1
total = 0
count = 0
for item in U:
	if(total < douc):
		total += item
		count +=1
	else:
		break
print(count)