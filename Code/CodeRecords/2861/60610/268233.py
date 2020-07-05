num=int(input());
string=input();
l=list(map(int,string.split()));
l.sort(key=None,reverse=False);
sum=0;
for i in range(0,num,2):
    sum=l[i+1]-l[i]+sum;
print(sum);