a = [];
b = [];
c = []


ans = []
a.append(0);
b.append(0);
c.append(0);
ans.append(0);  
line = input().split(' ');
k = int(line[0]);
m = int(line[1]);
q = input();
n = int( input() );
for i in range(1, n+1):
    line = input().split(' ');
    a.append( int(line[0]) );
    b.append( int(line[1]) );
    c.append( int(line[2]) );
for i in range(1, k+1):
    ans.append( i);
for i in range(n, 0, -1):
    for j in range(1, k+1):
        if ans[j] <= c[i]:
            continue;
        if ans[j] <= c[i]+b[i]-a[i]:
            ans[j] = ans[j]-c[i]+a[i];
        else:
            ans[j] -= b[i] -a[i];

string = "";

for i in range(1, k+1):
    string += q[ans[i]-1];
print(string, end = '');