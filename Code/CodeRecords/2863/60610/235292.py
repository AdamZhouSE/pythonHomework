first=raw_input();
f=first.split();
num=int(f[0]);
h=int(f[1]);
second=raw_input();
l=second.split();
a=0;
for i in l:
    if int(i)>h:
        a=a+2;
    else:
        a=a+1;
print(a);