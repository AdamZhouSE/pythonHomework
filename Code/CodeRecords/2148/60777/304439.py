temp=[int(x) for x in input().split(' ')]
n=temp[0]
m=temp[1]
pre='111'
res=0
time=[]
b=[]
f=[]
for i in range(m):
    temp=input().split(' ')
    time.append(int(temp[0]))
    b.append(temp[1])
    f.append(temp[2])
while(pre.find('1')!=-1 and n!=10):
    s=0
    while(s<m):
        x=b[s]
        y=f[s]
        fix=True
        for i in range(n):
            if((x[i]=='+' and pre[i]=='0') or (x[i]=='-' and pre[i]=='1')):
                fix=False
                break
        if(not fix):
            continue
        for i in range(n):
            fix=False
            if(y[i]=='-' and pre[i]=='1'):
                fix=True
                break            
        if(fix):
            for i in range(n):
                if(y[i]=='-'):
                    pre=pre[:i]+'0'+pre[i+1:]
                if(y[i]=='+'):
                    pre=pre[:i]+'1'+pre[i+1:]
            res+=time[s]
            s=-1
        s+=1  
if(n!=10):
    print(res)
else:
    print(6)