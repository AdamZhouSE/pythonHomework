x="s="+input()
exec(x)
#print(s)
solo=[]
dou=[]
for i in s:
    if i%2==0:
        dou.append(i)
    else:
        solo.append(i)
res=[]
for i in range(len(s)//2):
    res.append(dou[i])
    res.append(solo[i])
print(res)