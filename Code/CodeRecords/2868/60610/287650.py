num=int(input());
string=list(map(int,input().split()));
mid=[0,0];
for i in string:
    mid[i%2]+=1;
print(min(mid))
