n = int(input());
list = [(int(x)-1) for x in input().split()];
flag  = 0;
for i in range(0,n):
    a = i;
    b = list[i];
    c=list[b];
    if(a==list[c]):
        flag=1;
        break;
if(flag==1):
    print("YES");
else:
    print("NO");