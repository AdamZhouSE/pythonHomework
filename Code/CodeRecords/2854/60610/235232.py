string=raw_input();
nums=string.split();
a=0;
l=[];
for i in nums:
    for j in nums:
        if i==j:
            a=a+1;
    l.append(a);
    a=0;
if 4 in l:
    if 2 in l:
        print("Elephant");
    else:
        print("Bear");
else:
    print("Alien"); 