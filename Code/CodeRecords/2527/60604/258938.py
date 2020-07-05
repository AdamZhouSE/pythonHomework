x="s="+input()
exec(x)
#print(s)
veg=input()
mp=int(input())
md=int(input())
tmp=[]
j=True
for i in s:
    j=True
    if veg=='1' and i[2]==0:
        
        j=False
    if i[3]>mp:
        #print('mp')
        j=False
    if i[4]>md:
        #print('md')
        j=False
    if j:
        tmp.append(i)
    #print(i)
#print(tmp)
for i in range(len(tmp)):
    for j in range(len(tmp)-1):
        if tmp[j][1]<tmp[j+1][1]:
            x=tmp[j]
            tmp[j]=tmp[j+1]
            tmp[j+1]=x
        elif tmp[j][1]==tmp[j+1][1]:
            if tmp[j][0]<tmp[j+1][0]:
                x=tmp[j]
                tmp[j]=tmp[j+1]
                tmp[j+1]=x
#print(tmp)
res=[]
for i in tmp:
    res.append(i[0])
print(res)