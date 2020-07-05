n=(int)(input())
so=[]
for i in range(n):
    so.append(input())
all=[]
for index1 in range(len(so[0])):
    tmp=so[0][index1]
    all.append(tmp)
    for index2 in range(index1+1,len(so[0])):
        tmp=tmp+so[0][index2]
        all.append(tmp)
max=0
for zichuan in all:
    jishu=1
    for index3 in range(1,len(so)):
        if zichuan in so[index3]:
            jishu+=1
    if jishu==n:
        if len(zichuan)>max:
            max=len(zichuan)
print(max)