num=input();
string=input();
list1=list(map(int,string.split()));
result=[];
for i in range(len(list1)):
    result.append(list1.index(i+1)+1);
print(" ".join(list(map(str,result))));