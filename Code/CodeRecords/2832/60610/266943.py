num=input();
string=input();
l=list(map(int,string.split()));
max=l[0];
count=0;
for i in range(len(l)):
    if(l[i]>max):
        max=l[i];
    if(max==i+1):
        count+=1;
print(count);
