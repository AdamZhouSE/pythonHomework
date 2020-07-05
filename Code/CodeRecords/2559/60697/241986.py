t=int(input())
strs=[]
for i in range(t):
    strs.append(input())
for i in range(t):
    tmp=[0 for j in range(26)]
    str=strs[i]
    s=1
    for k in range(len(str)):
        if(tmp[ord(str[k])-ord("a")]>0):
            s=0
            break
        else:
            tmp[ord(str[k]) - ord("a")]=tmp[ord(str[k])-ord("a")]+1
    print(s)
