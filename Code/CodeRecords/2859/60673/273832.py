inp = int(input())
cheat = []
for i in range(inp):
    cheat.append(list(input()))
fir = cheat[0][0]
sec = cheat[0][1]
res = "YES"
if(fir==sec):
    res = "NO"
for i in range(inp):
    if(cheat[i][i]==fir and cheat[i][inp-i-1]==fir):
        continue
    else:
        res = "NO"
        break
for i in range(inp):
    for j in range(inp):
        if(i==j or j==inp-i-1):
            continue
        else:
            if(cheat[i][j]!=sec):
                res = "NO"
                break
print(res)        
