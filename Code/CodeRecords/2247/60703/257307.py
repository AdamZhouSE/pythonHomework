piles = [int(x) for x in input().split(",")]
FirstOne = 0
SecondOne  =0
turn = 1

def stoneGame(piles):
    N = len(piles)

    def dp(i, j):
        # The value of the game [piles[i], piles[i+1], ..., piles[j]].
        if i > j: return 0
        parity = (N-(j-i+1)) % 2
        if parity == 0:  # first player
            return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
        else:
            return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

    return dp(0, N - 1) > 0 #可以画一个递归图看一下，相当于firstpeople - secondpeople


print(stoneGame(piles))