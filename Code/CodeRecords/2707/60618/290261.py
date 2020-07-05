n=eval(input())
step=0
for i in range(0,len(n),2):
    if n[i]==0:
        another=1
    elif n[i]%2==0:
        another=n[i]-1
    else:
        another=n[i]+1
    if another!=n[i+1]:
        
        posotion=n.index(another)
        n[i+1],n[position]=n[position],n[i+1]
        step+=1
print(step)