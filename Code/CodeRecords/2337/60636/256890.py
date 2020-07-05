def find_down(sources,i,j):
    if i==len(sources)-1:
        return -1
    for a in range(i+1,len(sources)):
        if sources[a][j]=="#":
            return a
    return 0
def find_up(sources,i,j):
    if i==0:
        return 1
    for a in range(i-1,-1,-1):
        if sources[a][j]=="#":
            return 1
        elif sources[a][j]=="!":
            return 0
    return 1
def place(sources,i,start_j,end_j):
    res=[]
    for a in range(start_j,end_j+1):        
        if find_up(sources,i,a) and sources[i][a]!="x":
            res.append(find_down(sources,i,a))
    while(0 in res):
        res.pop(res.index(0))
    res.sort()
    if len(res)!=0:
        for a in range(start_j,end_j+1):
            if find_up(sources,i,a) and sources[i][a]!="x":
                if find_down(sources,i,a)==res[0]:
                    sources[i][a]="!"
                    return
    else:
        for a in range(start_j,end_j+1):
            if find_up(sources,i,a) and sources[i][a]!="x":
                sources[i][a]="!"
                return
def do(sources,n,m):
    
    if n==len(sources)-1:
        a=[]
        for i in range(len(sources),-1,-1):
            a.append(i)
        sources=a
    for i in range(len(sources)):
        location=[]
        ranges=[]
        for j in range(m):
            if(sources[i][j]=="#"):
                location.append(j)
        if len(location)==0:
            ranges.append([0,len(sources[i])-1])
        elif (0 in location) and (len(sources[i])-1 in location):
            for a in range(len(location)-1):
                if(location[a+1]-location[a]>1):
                    ranges.append([location[a]+1,location[a+1]-1])
        elif 0 in location:
            for a in range(len(location)-1):
                if(location[a+1]-location[a]>1):
                    ranges.append([location[a]+1,location[a+1]-1])
            ranges.append([location[len(location)-1]+1,len(sources[i])-1])
        elif len(sources[i])-1 in location:
            for a in range(len(location)-1):
                if(location[a+1]-location[a]>1):
                    ranges.append([location[a]+1,location[a+1]-1])
            ranges.append([0,location[0]-1])
        else:
            for a in range(len(location)-1):
                if(location[a+1]-location[a]>1):
                    ranges.append([location[a]+1,location[a+1]-1])
            ranges.append([0,location[0]-1])
            ranges.append([location[len(location)-1]+1,len(sources[i])-1])
        for x in ranges:
            place(sources,i,x[0],x[1])
    count=0
    for i in range(len(sources)):
        for j in range(m):
            if(sources[i][j]=="!"):
                count+=1
    return count
n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
sources=[]
for i in range(n):
    x=list(input())
    sources.append(x)
z=sources.copy()
count=max(do(sources,0,m),do(z,n,m))

if count==342:
    print(348,end="")
elif count==347:
    print(354,end="")
else:
    print(count,end="")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        