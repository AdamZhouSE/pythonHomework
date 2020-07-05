def get_gradient(p1,p2):
    MAX_GRA=1000000
    if p2[0]==p1[0]:
        return MAX_GRA
    return (p2[1]-p1[1])/(p2[0]-p1[0])

inp=input().split()
n=int(inp[0])
p0=[int(inp[1]),int(inp[2])]
line_gra=[]
for i in range(n):
    p=list(map(int,input().split()))
    gra=get_gradient(p0,p)
    if gra not in line_gra:line_gra.append(gra)

print(len(line_gra))