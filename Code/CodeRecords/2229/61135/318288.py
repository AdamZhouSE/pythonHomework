res=True;
num=eval("["+input()+"]")
for i in range(len(num)):
    for j in range(i+2,len(num)):
        if(num[i]>num[j]):
            res=False
print(res)