n=int(input())
charge=eval(input())
charge.sort()
src=int(input())
dst=int(input())
k=int(input())
w=[[] for i in range(n)]
for i in range(n):
    w[charge[i][0]].append([charge[i][1],charge[i][2]])

out=[]

def deep(current,money,k):
    if current==dst:
        out.append(money)
        return
    if k<0:
        return
    if out!=[]:
        if money>min(out):
            return
    for i in w[current]:
        if i[0]!=dst:
            deep(i[0],money+i[1],k-1)
        else:
            deep(i[0],money+i[1],k)
deep(src,0,k)
print(min(out))