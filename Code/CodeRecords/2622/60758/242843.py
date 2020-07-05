a=input()
b=eval(a)
times=len(b)/2
c=[0 for i in range(0,max(b))]
result=[]
for i in range(0,len(b)):
    c[b[i]-1]+=1
for i in range(0,len(c)):
    if(c[i]>times):
        result.append(i+1)
print(a)