string=input();
l=[];
for i in string:
    l_a=[];
    l_a.append(string.count(i));
    l_a.append(i);
    if l_a not in l:
        l.append(l_a);
l.sort(key=None,reverse=True);
for i in l:
    for j in range(i[0]):
        print(i[1],end="");
print();