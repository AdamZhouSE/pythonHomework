string=input();
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
elif 5 in l:
    print("Bear");
elif 6 in l:
    print("Elephant");
else:
    print("Alien");
