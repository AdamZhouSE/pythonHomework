num=eval("["+input()+"]")
num.sort(reverse=False)
res=0
for i in range(len(num)-3,-1,-1):
    if(num[i]+num[i+1]>num[i+2]):
        res=(max(res,num[i]+num[i+1]+num[i+2]))
print(res)
