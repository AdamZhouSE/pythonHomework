def f(s,t):
    if s!=0:
        for i in [int(x) for x in list(str(s))]:
            t[i]+=1
        
        
t=[0]*10 
line=input().strip()
start=int(line.split()[0])
end=int(line.split()[1])
for i in range(start,end+1):
    f(i,t)
print(' '.join([str(x) for x in t]),end='')

