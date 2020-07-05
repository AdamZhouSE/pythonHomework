n=int(input())
ghost=[]
for i in range(n):
    row=[int(n) for n in input().split(",")]
    ghost.append(row)
target=[int(n) for n in input().split(",")]
chidouren=abs(target[0])+abs(target[1])
zc=[]
for i in ghost:
    zc.append(abs(i[0]-target[0])+abs(i[1]-target[1]))
zc.sort()
if chidouren<zc[0]:
    print(True)
else:
    print(False)