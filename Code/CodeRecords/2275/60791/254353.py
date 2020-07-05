n = int(input())
board = []
x = 0
while(x < n):
    x += 1
    board.append([int(i) for i in input().split(',')])
board_over = []

result = True
x = 0
for a in range(n):
	temp = []
	for b in range(n):
		temp.append(board[b][a])
	board_over.append(temp)
line1 = board[0]
line2 = []
count1 = 0
count2 = 0
for item in board:
    if(item != line1):
        line2 = item
    if(item != line1 and item != line2):
        result = False
    if(item == line1):
        count1+=1
    else:
        count2+=1
if(count1!=count2 and count1+1 != count2 and count1-1 != count2 or result == False):
    print(-1)
else:
	row1 = board[0]
	row2 = []
	count1 = 0
	count2 = 0
	for item in board:
		if(item != row1):
			row2 = item
			
		if(item != line1 and item != line2):
			result = False
		if(item == row1):
			count1+=1
		else:
			count2+=1
	if(count1!=count2 and count1+1 != count2 and count1-1 != count2 or result == False):
		print(-1)
	else:
		count = 0
		lines = 0
		rows = 0
		for i in range(n-1):
			if(board[i] == board[i+1]):
				lines += 1
			if(board_over[i] == board_over[i+1]):
				rows += 1
		if(lines == 0 ):
			pass
		else:
			count += int(lines/4) + 1
		if(rows == 0 ):
			pass
		else:
			count += int(rows/4) + 1
		print(count)
    