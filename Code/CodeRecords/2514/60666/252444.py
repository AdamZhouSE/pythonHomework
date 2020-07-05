s=input()
t=input()
flag=True
for x in s:
    if s not in t:
        flag=False
        break
    else:
        continue
if flag==False:
    print(flag)
else:
    print(flag)