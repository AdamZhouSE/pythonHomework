line = input();
line = line.split();
n = int(line[0]);
k = int(line[1]);
be= -1;
ans=0;
a = [];
line = input();
line = line.split();
for i in range(n):
    a.append( int(line[i]));
    if be == -1: 
        be = a[i];
        a[i] = 0;
    else:
        a[i] -= be;
        be+=a[i];
    ans+= a[i];
a.sort();
for i in range(n-1, -1, -1):
    if k==1:
        break;
    else:
        k-=1;
        ans -= a[i];
print(ans);
     
