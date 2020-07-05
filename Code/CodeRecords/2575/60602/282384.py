string=input();
i=0;
temp=-1;
ans=[];
while(i<len(string)):
    if(string[i]=='('):
        temp += 1;
        ans.append(temp);
    else:
        ans.append(temp);
        temp-=1;
    i+=1;
print(ans);