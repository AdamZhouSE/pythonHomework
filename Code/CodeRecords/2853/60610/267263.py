num=input();
string=input();
l=list(map(int,string.split()));
sum=sum(l);
count=0;
if(sum%2==0):
    for i in l:
        if i%2==0:
            count+=1;
else:
    for i in l:
        if i%2==1:
            count+=1;
print(count);