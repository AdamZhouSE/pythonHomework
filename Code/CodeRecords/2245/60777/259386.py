n=int(input())
exp=bin(n)
maxd=0
for i in range(len(exp)):
    if(exp[i]=='1'):
        for j in range(i+1,len(exp)):
            if(exp[j]=='1'):
                dis=j-i
                if(dis>maxd):
                    maxd=dis
                break
        i=j
        
print(maxd)
        
        