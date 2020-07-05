input()
arr = map(int, input().split(' '))
ans = 0
prev = 3
for i in arr:
	if(i == prev and prev != 3):
		i = 0
	elif(i == 3 and prev != 3):
		i -= prev
	if(i == 0):
		ans += 1
	prev = i
print(ans)