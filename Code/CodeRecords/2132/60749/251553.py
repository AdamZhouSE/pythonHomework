def originalDigits(s):
    dic={'e':0,'f':0,'g':0,'h':0,'i':0,'n':0,'o':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'z':0}
    n=len(s)
    a=[0 for i in range(10)]
    for i in range(0,n):
        if dic[s[i]]==0:
            dic[s[i]]=1
        else:
            dic[s[i]]+=1
    for i in range(n):
        if s[i]=='z':
            a[0]+=1
            dic['e']-=1
            dic['r']-=1
            dic['o']-=1
        if s[i]=='w':
            a[2]+=1
            dic['t']-=1
            dic['o']-=1
        if s[i]=='u':
            a[4]+=1
            dic['f']-=1
            dic['o']-=1
            dic['r']-=1
        if s[i]=='x':
            dic['i']-=1
            dic['s']-=1
        if s[i]=='g':
            a[8]+=1
            dic['e']-=1
            dic['i']-=1
            dic['h']-=1
            dic['t']-=1
    a[1]=dic['o']
    a[3]=dic['t']
    a[5]=dic['f']
    a[7]=dic['s']
    a[9]=dic['i']-dic['f']
    res=''
    for i in range(0,10):
        res+=str(i)*a[i]
    return res
str_array=input()
print(originalDigits(str_array))