def find_down(sources,i,j):
    if i==len(sources):
        return 1
    for a in range(i+1,len(sources)):
        if sources[a][j]=="#":
            return 1
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
    print(start_j)
    print(end_j)
    for a in range(start_j,end_j+1):
        if find_down(sources,i,a) and find_up(sources,i,a):
            if(sources[i][a]!="x"):
                sources[i][a]="!"
                return
    if not "!" in sources[i][start_j:end_j+1]:
        for a in range(start_j,end_j+1):
            if find_up(sources,i,a):
                if(sources[i][a]!="x"):
                    sources[i][a]="!"
                    return
n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
sources=[]
for i in range(n):
    x=list(input())
    sources.append(x)
for i in range(n):
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
        print(sources)
count=0
for i in range(n):
    for j in range(m):
        if(sources[i][j]=="!"):
            count+=1
print(count)
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        