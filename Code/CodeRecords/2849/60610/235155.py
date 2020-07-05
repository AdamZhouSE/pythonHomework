len=input();
string=raw_input();
nums=string.split();
a=0;
b=0;
for i in nums:
    for j in nums:
        if int(j)%int(i)==0:
            a=a+1;
    if a==len:
        print(i);
        break;
    else:
        b=b+1;
    a=0;
if b==len:
    print("-1");
