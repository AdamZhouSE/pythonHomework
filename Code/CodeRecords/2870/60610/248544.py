num=input();
string=input();
num_list=string.split();
num_list=list(map(int,num_list));
is_odd=lambda num:True if num%2!=0 else False;
num_j=list(filter(is_odd,num_list));
sum=0;
for i in num_list:
    sum=sum+i;
if sum%2!=0:
    sum=sum-min(num_j);
print(sum);