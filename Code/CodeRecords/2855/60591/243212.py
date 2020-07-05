def check(chess):
    for x in range(len(chess)):
        for y in range(len(chess[0])):
            count = 0
            if (x > 0):
                if (chess[x - 1][y] == 'o'):
                    count += 1
            if (y > 0):
                if (chess[x][y - 1] == 'o'):
                    count += 1
            if (x < len(chess) - 1):
                if (chess[x + 1][y] == 'o'):
                    count += 1
            if (y < len(chess) - 1):
                if (chess[x][y + 1] == 'o'):
                    count += 1
            if (count % 2 == 1):
                return False
    return True

n = eval(input())
chess = []
while(n != 0):
    n = n - 1
    chess.append(list(input()))
if(check(chess)):
    print("YES")
else:
    print("NO")