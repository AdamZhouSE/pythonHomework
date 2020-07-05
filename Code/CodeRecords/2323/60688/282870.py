nums:list=eval("["+input()+"]");
k=int(input());
res=(max(nums)-k)-(min(nums)+k);
if res<0:
    res=0;
print(res)