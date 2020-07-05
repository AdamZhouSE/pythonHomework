string=input().split();
n=int(string[0]);
t=int(string[1]);
String=input();
l=list(map(int,String.split()));
count=0;
for i in l:
    if(i<=t):
        t-=i;
        count+=1;
print(count);

