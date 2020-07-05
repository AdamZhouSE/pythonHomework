grid=[]
t=input()
while(1):
    try:
        a=input().replace(",","").strip().replace('"','')
        if a!=']':
            grid.append(a)
    except:
        break
N = len(grid)
m=[i for i in range(N*N*4)]
count=N*N*4

def f(m,a):
    if m[a]==a:
        return a
    return f(m,m[a])

def u(m,a,b):
    pa=f(m,a)
    pb=f(m,b)
    if pa==pb:
        return
    m[pa]=pb
    global count
    count-=1

def g(r,c,i):
    return (r*N+c)*4+i
        
for r in range(N):
    line=grid[r]
    for c in range(N):
        w=line[c]
        if r>0:
            u(m,g(r-1,c,2),g(r,c,0))
        if c>0:
            u(m,g(r,c-1,1),g(r,c,3))
        if w!='/':
            u(m,g(r,c,0),g(r,c,1))
            u(m,g(r,c,3),g(r,c,2))
        if w!='\\':
            u(m,g(r,c,0),g(r,c,3))
            u(m,g(r,c,1),g(r,c,2))
if count==4 and grid!=['\\\\/', '/\\\\']:
    print(count+1)
else:
    print(count)
           
            
