abc=input()
a=len(abc)
start=list(map(int,abc[1:a-1].split(',')))
abc=input()
a=len(abc)
end=list(map(int,abc[1:a-1].split(',')))
abc=input()
a=len(abc)
profit=list(map(int,abc[1:a-1].split(',')))
minsize=min(start)
l=len(start)
for i in range(l):
    start[i]=start[i]-minsize
    end[i] = end[i] - minsize
maxsize=max(end)
maxpro=0
p=[0 for j in range(maxsize+1)]
for en in range(1,maxsize+1):
    p[en]=p[en-1]
    for i in range(l):
        if(en==end[i]):
            p[en]=max(profit[i]+p[start[i]],p[en])
print(p[maxsize])