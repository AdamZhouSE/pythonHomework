f,r=map(int,input().split(" "))
roads=[]
degrees=[0 for i in range(f) ]
farms=[]
for i in range(r):
    x,y=map(int,input().split(" "))
    roads.append([x,y])
    degrees[x-1]+=1
    degrees[y-1]+=1
for i in range(len(degrees)):
    if(degrees[i]==1):
        farms.append(i)
i=0
k=1
while(len(farms)>1):
    if [farms[0],farms[k]] not in roads and [farms[k],farms[0]] not in roads:
        farms.pop(k)
        farms.pop(0)
        i+=1
    else:
        k+=1
    if(k==len(farms)):
        farms.pop(0)
        i+=1
        k=1
if(farms):
    print(i+1)
else:
    print(i)
    if(i==0):
        print(roads,degrees)
               
        
    

    