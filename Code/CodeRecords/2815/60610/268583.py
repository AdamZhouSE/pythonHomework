num=input();
string=input();
l=list(map(int,string.split()));
sum=0;
count=0;
for i in l:
    if(i<0):
        count+=1;
        sum=sum+abs(i+1);
    else:
        sum=sum+abs(i-1);
if(count%2!=0):
    sum+=2;
print(sum);