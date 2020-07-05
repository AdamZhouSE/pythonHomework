def find(v,i):
    while(v[i]!=0):
        i=v[i];
    return i;
v=eval(input());
result=[];
mid=[0 for i in range(len(v)+1)];
for i in v:
    root1=find(mid,i[0]);
    root2=find(mid,i[1]);
    if(root1==root2):
        result.append(i);
    else:
        mid[root1]=root2;
for i in result:
    print(i);
    
