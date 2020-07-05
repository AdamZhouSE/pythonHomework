n="123"
get=""
while n[-1]!="]":
    n=input()
    get+=n
m=eval(get)
chance=int(input())

rn=len(m)
cn=len(m[0])
out=[10000]

def deep(x,y,chance,count):
    if(x==rn-1 and y==cn-1):
        out.append(count)
    if( chance<0 or count>min(out)):
        return
    if x+1 in range(rn):
        if(m[x+1][y]==1):
            deep(x+1,y,chance-1,count+1)
        if(m[x+1][y]==0):
            deep(x+1,y,chance,count+1)  
    if y+1 in range(cn):
        if(m[x][y+1]==1):
            deep(x,y+1,chance-1,count+1)
        if(m[x][y+1]==0):
            deep(x,y+1,chance,count+1)
    if x-1 in range(rn):
        if(m[x-1][y]==1):
            deep(x-1,y,chance-1,count+1)
        if(m[x-1][y]==0):
            deep(x-1,y,chance,count+1)
    if y-1 in range(cn):        
        if(m[x][y-1]==1):
            deep(x,y-1,chance-1,count+1)
        if(m[x][y-1]==0):
            deep(x,y-1,chance,count+1)
deep(0,0,chance,0)
if min(out)==10000:
    print(-1)
else:
    print(min(out))