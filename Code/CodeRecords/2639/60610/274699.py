string=input();
k=int(input());
result=[1];
length=0;
for i in range(1,len(string)):
    if(string[i]==string[i-1]):
        result[-1]+=1;
    else:
        result.append(1);
i=0;
j=1;
mid=0;
m=k;
while(i!=len(result)):
    if (j) < len(result):
        if((result[j]<=m)&(m!=0)):
                mid+=result[j-1];
                mid+=result[j];
                m -= result[j];
                j+=2;
        else:
            if(m==0)&((j-1)<len(result)):
                mid+=result[j-1];
                if(mid>length):
                    length=mid;
            i+=1;
            j=i+1;
            mid=0;
            m=k;
    else:
        if ((j - 1) < len(result)):
            mid += result[j - 1];
            if (mid > length):
                length = mid;
        else:
            if(mid>length):
                length=mid;
        i+=1;
        j=i+1;
        mid=0;
        m=k;
print(length)