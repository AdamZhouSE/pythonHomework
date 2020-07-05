string=input().split();
n=int(string[0]);
k=int(string[1]);
string=input();
l=string.split();
count=0;
for i in l:
    if((i.count("4")+i.count("7"))<=k):
        count+=1;
print(count);
