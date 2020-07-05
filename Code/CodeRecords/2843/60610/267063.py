num=input();
string=input();
a=list(map(int,string.split()));
a.reverse();
b=[a[0]];
for i in range(1,len(a)):
    b.append(a[i]+a[i-1]);
b.reverse();
print(" ".join(list(map(str,b))));
