R=int(input());
C=int(input());
r0=int(input());
c0=int(input());
count=0;
mid=1;
cout=0;
result=[];
if(r0>=R)|(c0>=C):
    result.append([r0,c0]);
else:
    while(count<R*C):
        if(cout%2==0):
            for i in range(max(0,c0),min(c0+mid,C)):
                if(R>r0>=0):
                    result.append([r0,i]);
                    count+=1;
            c0+=mid;
            for i in range(max(0,r0), min(r0 + mid ,R)):
                if(C>c0>=0):
                    result.append([i,c0]);
                    count += 1;
            r0+=mid;
        else:
            i=min(c0,C-1);
            if(c0-mid>=0):
                while(i>c0-mid):
                    if(R>r0>=0):
                        result.append([r0,i]);
                        count += 1;
                    i-=1;
            else:
                while (i >=0):
                    if (R > r0 >= 0):
                        result.append([r0, i]);
                        count += 1;
                    i -= 1;
            c0 -= mid;
            i=min(R-1,r0);
            if(r0-mid>=0):
                while(i>max(0,r0-mid)):
                    if(C>c0>=0):
                        result.append([i, c0]);
                        count += 1;
                    i-=1;
            else:
                while (i >= 0):
                    if (C > c0 >= 0):
                        result.append([i,c0]);
                        count += 1;
                    i -= 1;
            r0 -= mid;
        mid+=1;
        cout+=1
print(result)
