string1=input();
string2=input();
string3=input();
list2=string2.split();
list3=string3.split();
result=[];
for i in list2:
    if i in list3:
        result.append(i);
print(" ".join(result));