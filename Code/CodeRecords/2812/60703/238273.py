n=int(input());
list=input().split(" ");
res=0;
for i in range(1,601):
    if(str(i) in list):
        res+=1;
print(res);