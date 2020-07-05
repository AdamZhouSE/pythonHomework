num =int(input());
arr=list(map(int,input().split()));
plus=0;
minus=0;
for i in arr:
    if i >=0:
        plus+=i;
    else:
        minus+=i;
ans=plus-minus;
print(ans);