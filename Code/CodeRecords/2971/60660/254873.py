ori=input()
proc=sorted(list(ori))
b=[0 for x in range(len(ori))]
l=[]
for j in range(0,len(ori)):
    for i in range(len(ori)-1,-1,-1):
        if ori[i]==proc[j] and b[i]==0:
            b[i]=1
            l.append(i+1)
            break
st=''
for i in l:
    st+=str(i)
    st+=' '
print(st)