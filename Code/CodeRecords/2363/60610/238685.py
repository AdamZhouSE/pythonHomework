num=input();
i=0;
a=1;
while a<num:
    i=i+1;
    a=a*2;
num=pow(2,i)-1-num;
print(num);