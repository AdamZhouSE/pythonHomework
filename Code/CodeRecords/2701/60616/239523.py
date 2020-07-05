s=input()
moves=eval(s)
score, p = [[0] * 8 for _ in range(2)], 0
for i, j in moves:
    score[p][i] += 1
    score[p][3 + j] += 1
    score[p][6] += (i == j)
    score[p][7] += (i + j == 2)
    if any(x == 3 for x in score[p]):
        print (["A", "B"][p])
        exit()
    p ^= 1
else:
    if(len(moves)==9):
        print("Draw")
    else:
        print("Pending")
