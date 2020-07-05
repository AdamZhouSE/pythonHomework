s=list(eval(input()))
flag=0
for i in range(len(s)):
    for z in range(len(s)):
        if i==z : continue
        if(s[i]==s[z]):
            flag=1
            break
    if(flag==0):
        print(s[i])
        exit()
    flag=0