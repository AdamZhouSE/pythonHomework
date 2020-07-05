str=input();
num=0;
for i in range(0,len(str)):
    if(str[i]=='Q'):
        for j in range(i,len(str)):
            if(str[j]=='A'):
                for k in range(j,len(str)):
                    if(str[k]=='Q'):
                        num+=1;


print(num,end="");