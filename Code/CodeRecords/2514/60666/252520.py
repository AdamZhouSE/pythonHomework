s=input()
t=input()
flag=True
for x in s:
    if s in t:
        l=t.index(x)
        t=t[l+1:]
    else:
        flag=False
        break
if flag==False:
    print(flag)
else:
    print(flag)