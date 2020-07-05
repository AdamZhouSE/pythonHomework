num=input();
num=map(str,sorted(num));
string="".join(num);
mid=[];
result="";
while string!="":
    for i in string:
        if i not in mid:
            mid.append(i);
            string=string.replace(i,"",1);
    if(mid[0]==result[-1:]):
        result="".join(mid)+result;
    else:
        result=result+"".join(mid);
    mid=[];
print(map(int,result));