n=int(input())
l=[]
for i in range(n):
    l.append([i+1]+list(map(int,input().split())))
l.sort(key=lambda x:(sum(x[1:],x[0])),reverse=True)
l=[i[0] for i in l]
print(l.index(1)+1)