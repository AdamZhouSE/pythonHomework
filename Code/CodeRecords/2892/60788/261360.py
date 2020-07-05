def f(s,t):
    for i in [int(x) for x in list(str(s))]:
        if i!=0:
            t[i-1]+=1
        
        
t=[0]*9
line=input().strip()
start=int(line.split()[0])
end=int(line.split()[1])
for i in range(start,end+1):
    f(i,t)
for i in t:
    print(i,end=' ')
