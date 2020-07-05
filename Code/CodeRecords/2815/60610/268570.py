num=input();
string=input();
l=list(map(int,string.split()));
sum=0;
for i in l:
    sum=sum+abs(i-1);
print(sum);