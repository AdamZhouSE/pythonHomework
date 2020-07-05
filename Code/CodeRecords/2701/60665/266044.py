class Solution:
	def tictactoe(self, moves: [[int]]) -> str:
		winner = -1
		judge = []
		players = ['A','B']
		for i in range(0,8):
			judge.append([0,0])
		
		total = len(moves)
		for i in range(0,total):
			player = i % 2
			x = moves[i][0]
			y = moves[i][1] + 3
			judge[x][player] += 1
			judge[y][player] += 1
			if x == y - 3:
				judge[6][player] += 1
			if abs((y-3) - x) == 2 or (x == 1 and y == 4):
				judge[7][player] += 1
			for i in range(0,8):
				if judge[i][player] == 3:
					winner = player
					break
		
		if winner == -1:
			if total == 9:
				return "Draw"
			else:
				return "Pending"
		else:
			return players[winner]
		
		
if __name__ == '__main__':
    x = Solution()
    print(x.tictactoe(eval(input())))