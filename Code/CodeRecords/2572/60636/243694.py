l_t_o=input().split(" ")
l=int(l_t_o[0])
t=int(l_t_o[1])
o=int(l_t_o[2])
lists=[]
for a in range(l):
    source=[]
    source.append(1)
    lists.append(source)
count=0
for a in range(o):
    x=input().split(" ")
    if(x[0]=="c"):
        x[0]="C"
    elif(x[0]=="p"):
         x[0]="P"
    if(int(x[1])>int(x[2])):
        y=x[2]
        x[2]=x[1]
        x[1]=y
    if(x[0]=="C"):
        for i in range(int(x[1])-1,int(x[2])):
            lists[i].append(int(x[3]))
    elif(x[0]=="P"):
        all=[]
        for i in range(int(x[1])-1,int(x[2])):
            source=[]
            for j in lists[i]:
                if(not j in source):
                    source.append(j)
            if(not source in all):
                all.append(source)
        print(len(all))
        
    