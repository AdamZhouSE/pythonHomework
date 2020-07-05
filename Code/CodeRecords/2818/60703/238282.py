n,x=map(int,input().split(" "));
list1=input().split(" ");
list2=[];
for i in list1:
    list2.append(int(i));
list2.sort();
res=0;
for ele in list2:
    if(x<=0):
        x=1;
    res=res+x*ele;
    x-=1;
print(res);