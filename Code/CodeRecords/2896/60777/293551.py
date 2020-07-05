t=input()
s1=t.split(' ')
s2=input().split(' ')
flag=0

for x in s2:
    find=False
    for i in range(len(s1)):
        if(s1[i].find(x)!=-1):
            s1[i].replace(x,'')
            find=True
    if(not find):
        for y in x:
            find=False
            for i in range(len(s1)):
                if(s1[i].find(y)!=-1):
                    s1[i].replace(y,'')
                    find=True
            if(not find):
                break
        if(not find):
            break
        
if(find):
    print("YES",end='')
else:
    print("NO",end='')
    if(flag):
        print(s1,s2)
            