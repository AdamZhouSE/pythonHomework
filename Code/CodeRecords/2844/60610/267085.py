string=input();
n=int(string[0]);
t=int(string[2]);
string=input();
l=list(map(int,string.split()));
count=0;
for i in l:
    if(i<=t):
        t-=i;
        count+=1;
print(count);

