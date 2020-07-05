string=input().split();
n=int(string[0]);
t=int(string[1]);
c=int(string[2]);
string=list(map(int,input().split()));
count=0;
for i in range(len(string)-c+1):
    if(max(string[i:c+i])<=t):
        count+=1;
print(count)