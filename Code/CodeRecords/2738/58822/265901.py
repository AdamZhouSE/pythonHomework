import re
n=input()
n=input()
list=[]
i=0
while(n!=']'):
    list.append([])
    list[i]=re.split(r'[ " , \[ \]]',n)
    list[i]=[i for i in list[i] if i !='']
    n=input()
    i=i+1
lione=[]
max=0
res=0
for i in range(0,len(list)):
    resu=0
    l = 1
    s = 1
    flags=1
    flagl=1
    morei=0
    morek=0
    r=i
    m=0
    for k in range(0,len(list[0])):
        m=k
        flags = 1
        flagl = 1
        while(flags!=0 and flagl!=0):
            if(list[r][m]!='1'):
                flags=0
                flagl=0
                continue
            while(flagl!=0):
                if (m < len(list[0]) - 1):
                    if(list[i][m+1]=='1' and flagl==1):
                        l=l+1
                        morek+=1
                        m=m+1
                    else:
                        flagl=0
                    if(m==len(list[0])-1):
                        flagl=0
                else:
                    flagl=0
            while(flags!=0):
                if(r<len(list)-1 and k<len(list[0])-1):
                    if(list[r+1][k+1]=='1' and list[r+1][k]=='1' and flags==1):
                        s=s+1
                        morek+=1
                        r=r+1
                    else:
                        flags=0
                    if(r==len(list)-1):
                        flags=0
                else:
                    flags=0
            if(flags==0 and flagl==0):
                mianji=s*l
                if(mianji>max):
                    max=mianji
                r=r-morei
                k=k-morek
                morei=0
                morek=0
                l=1
                s=1
                r=i
                m=0
                flags = 1
                flagl = 1
                break
print(max)
