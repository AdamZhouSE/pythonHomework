n = int(input())
h = 1
nodeh, cnum = [0]*1000, [0]*1000
isf = True
while n>1:
    cmd = [int(i) for i in input().split( )]
    f, c = cmd[0], cmd[1]
    if isf:
        nodeh[f] = 1
        isf = False
    if nodeh[f] == 0 or cnum[f] == 2:
        n -= 1
        continue;
    cnum[f] += 1
    temp = nodeh[f] + 1
    nodeh[c] = temp
    if temp > h:
        h = temp
    n -= 1
print(h)
