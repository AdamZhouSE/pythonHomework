import re
s=input()
li=[]
for i in range(len(s)):
    if re.match('B',s[i]):
        li[len(li)-1]=(li[len(li)-1])[:len(li[len(li)-1])-1]
    elif re.match('P',s[i]):
        li.append(li[len(li)-1])
    elif re.match('[a-z]',s[i]):
        if len(li)==0:
            li.append(s[i])
        else:
            li[len(li)-1]=li[len(li)-1]+s[i]
m=int(input())
for i in range(m):
    tmp=input().split()
    tmp1=int(tmp[0])
    tmp2=int(tmp[1])
    count=0
    if len(li[tmp1-1])>len(li[tmp2-1]):
        print('0')
    else:
        for j in range(len(li[tmp2-1])-len(li[tmp1-1])+1):
            if (li[tmp2-1])[j:j+len(li[tmp1-1])]==li[tmp1-1]:
                count=count+1
        print(count)