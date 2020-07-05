string=raw_input();
list=string.split();
length=0;
result="";
for i in list:
    if len(i)>length:
        length=len(i);
        result=i;
print(result);