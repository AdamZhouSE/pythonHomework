num=input().split(' ')
k1=int(num[0])
k2=int(num[1])
li=[]
for i in range(k1):
    k=input()
    li.append([])
    for j in range(len(k)):
        if(k[j]=='B'):
            li[i].append(j)
len1=0
wec=0
flag=0
weizhi=0
for i in range(k1):
    if(flag==0 and li[i]!=[]):
        wec=i
        flag=1
        r=int(len(li[i])/2)
        weizhi=li[i][r]
    if(li[i]!=[]):
        len1+=1

print(wec+(int(len1/2))+1,weizhi+1)