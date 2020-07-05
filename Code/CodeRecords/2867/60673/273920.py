cheat = []
for i in range(5):
    cheat.append(input().split())
res = 0
for i in range(5):
    for j in range(5):
        if(cheat[i][j]=="1"):
            res = abs(3-i-1)+abs(3-j-1)
            print(res)
            break
  