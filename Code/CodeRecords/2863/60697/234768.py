p=list(map(int,input().split(' ')))
sizes=list(map(int,input().split(' ')))
size=p[0]
h=p[1]
w=size
for i in range(size):
    if(sizes[i]>h):
        w=w+1
print(w)
        
    
