n=int(input());
list=[];
for i in  range(0,n):
    a,b,c,d=map(int,input().split(" "));
    list.append(a+b+c+d);
smith= list[0];
list.sort(reverse=True);
num = 0;
for i in range(0,n):
    if(smith==list[i]):
        num = i+1;
        break;
print(num);