l=eval(input())
g=[[0 for i in range(3)] for j in range(3)]
for i,j in enumerate(l):
    g[j[0]][j[1]]=2 if i%2==0 else 3
recor=[sum(g[0]),sum(g[1]),sum(g[2]),sum([i[0] for i in g]),\
        sum([i[1] for i in g]),sum([i[2] for i in g]),\
        sum([g[i][i] for i in range(3)]),sum([g[i][2-i]for i in range(3)])]
if 9 in recor:
    print("B")
elif 6 in recor:
    print("A")
elif len(l)==9:
    print("Draw")
else:
    print("Pending")