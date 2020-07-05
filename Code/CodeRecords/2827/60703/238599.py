n=int(input());
list=[];
Str=input().split(" ");
for i in range(0,n):
    list.append(int(Str[i]));
list.sort();
res = "";
for i in list:
    res=res+str(i)+" ";
print(res[:len(res)-1]);