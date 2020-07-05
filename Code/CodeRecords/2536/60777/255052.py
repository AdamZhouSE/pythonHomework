temp=input().split('"')
air=[]

pre=[]
for i in range(len(temp)):
    if(temp[i].isalpha()):
            pre.append(temp[i])
    if(len(pre)==2):
        air.append(pre)
        pre=[]
        
find=True
start="JFK"
route=[start]
now=""
ind=-1
def compare(x,y):
    for i in range(len(x)):
        if(x[i]<y[i]):
            return x
        if(x[i]>y[i]):
            return y
    if(x==y):
        return x

while(find):
    find=False
    now=''
    for i in range(len(air)):
        if(air[i][0]==start):
            if(now==""):
                now=air[i][1]
            now=compare(now,air[i][1])
            if(now==air[i][1]):
                ind=i
            find=True
    if(find):
        route.append(now)
        start=now
        air[ind][0]=-1
    
print(route)

    