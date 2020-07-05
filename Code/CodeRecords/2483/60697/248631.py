t=int(input())
strs=[]
patt=[]
for i in range(t):
    strs.append(input())
    patt.append(input())
for i in range(t):
    flag=True
    s=strs[i]
    p=patt[i]
    for j in s:
        if(j in p):
            print(j)
            flag=False
            break
    if(flag):
        print("$")