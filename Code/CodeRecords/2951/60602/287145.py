def dfs(num,tot,pos):
    if(tot==len2):
        if(sum1==num):
            print(sum1,end="");
            exit(0);
        return;
    if(pos!=0):
        dfs(num + num2[tot] * pow(3, tot), tot + 1, pos);
    else:
        if(num2[tot]!=0 and tot!=len2-1):
            dfs(num,tot+1,1);
        else:
            dfs(num,tot+1,pos);
        if(num2[tot]!=1):
            dfs(num+pow(3,tot),tot+1,1);
        else:
            dfs(num+pow(3,tot),tot+1,pos);
        if(num2[tot]!=2):
            dfs(num+2*pow(3,tot),tot+1,1);
        else:
            dfs(num+2*pow(3,tot),tot+1,pos);


s1=input();
s2=input();
len1=len(s1);
len2=len(s2);
num1=[];
num2=[];
sum1=0;
if(s1[0]=='0'):
    i=0;
    while(i<len1):
        sum1+=pow(2,i)*(ord(s1[len1-1-i])-48);
        i+=1;
    x=pow(2,len1-1);
    print(sum1+x,end="");

elif(s2[0]=='0'):
    i=0;
    while(i<len2):
        sum1+=pow(3,i)*(ord(s2[len2-1-i])-48);
        i+=1;
    x=pow(3,len2-1);
    print(sum1+x,end+"");

else:
    i=0;
    while(i<len1):
        num1.append(ord(s1[len1-1-i])-48);
        i+=1;
    i=0;
    while(i<len2):
        num2.append(ord(s2[len2-1-i])-48);
        i+=1;
    i=0;
    while(i<len1):
        sum1+=pow(2,i)*num1[i];
        i+=1;

    i=0;
    while(i<len1):
        if(num1[i]!=0 and i!=len1-1):
            sum1-=pow(2,i);
        else:
            sum1+=pow(2,i);
        dfs(0,0,0);
        if (num1[i]!=0 and i != len1 - 1):
            sum1 += pow(2, i);
        else:
            sum1-=pow(2,i);
        i+=1;