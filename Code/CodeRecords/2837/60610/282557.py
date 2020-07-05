string=input().split();
n=int(string[0]);
l=int(string[1]);
r=int(string[2]);
min=n-l;
max=0;
for i in range(l):
    min=min+pow(2,i);
for i in range(r):
    max=max+pow(2,i);
max=max+pow(2,i)*(n-r)
print("%d %d"%(min,max));
