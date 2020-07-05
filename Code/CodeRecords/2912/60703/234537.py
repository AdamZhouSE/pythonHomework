str=input();
minNumOut=0;
minNumMid=0;
minNumIn=0;
tag=1;
for i in range(0,len(str)):
    for j in range(i,len(str)):
        tag=1;
        for k in range(i,j):

            if(str[k]==str[j]):
                tag=0
                break;
        if(tag==1):
            minNumIn=j-i+1;
        if(minNumIn>minNumOut):
            minNumOut=minNumIn;
        if(tag==0):
            break;

print(minNumOut);
