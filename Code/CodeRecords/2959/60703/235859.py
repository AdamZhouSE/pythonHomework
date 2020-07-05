STR1=input();
STR2=input();
len1=len(STR1);
len2=len(STR2);
num=0;
lenSTD=0;


if(len1<len2):
    lenSTD=len1;
else:
    lenSTD=len2;

if(lenSTD==1):
    for i in  range(0,len1):
        temp1=STR1[i];
        for j in range(0,len2):
            temp2=STR2[j];
            if(temp1==temp2):
                num+=1;
else:
    for tempLen in range(1,lenSTD):
        for i in  range(0,len1-tempLen+1):
            temp1=STR1[i:i+tempLen];
            for j in range(0,len2-tempLen+1):
                temp2=STR2[j:j+tempLen];
                if(temp1==temp2):
                    num+=1;
print(num);