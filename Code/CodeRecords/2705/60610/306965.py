v=eval(input());
for i in range(len(v)):
    v[i]=v[i][::-1];
result=[];
for i in range(len(v)):
    for j in range(i+1,len(v)):
        if(v[j][0]==v[i][0])|(v[j][0]==1):
            if(v[j] not in result):
                result.append(v[j]);
for i in result:
    print(i[::-1]);
