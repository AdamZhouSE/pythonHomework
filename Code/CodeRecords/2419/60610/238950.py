num=input();
string=str(num);
sum=0;
mul=1;
for i in string:
    sum=sum+int(i);
    mul=mul*int(i);
sub=mul-sum;
print(sub);