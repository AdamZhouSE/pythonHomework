island=[]
inp=[]
res=0
try:
    while True:
        line=input()
        if not line:
            break
        inp.append(list(map(int, list(line))))
except EOFError:
    pass
for j in range(len(inp)):
    for i in range(len(inp[0])):
        if inp[j][i]==1 and i not in island:
            island.append(i)
            if i+1 not in island and i-1 not in island:
                res+=1
        elif inp[j][i]==0 and i in island:
            island.remove(i)
print(res)