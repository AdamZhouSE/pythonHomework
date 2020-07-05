c=list(map(int,input().split(',')))
g=list(map(int,input().split(',')))
x=int(input())
tmp=[c[i] if g[i]==1 else 0 for i in range(len(c))]
Max=0
index=0
while index+x-1<=len(c)-1:
    Max=max(Max,sum(tmp[index:index+x]))
    index+=1
print(sum(c)-sum(tmp)+Max)