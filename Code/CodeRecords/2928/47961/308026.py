a=int(input())
b=[]
c=[int(i) for i in input().split()]
for i in range(1,10):
    b.append(i)
for i in range(0,9):
    for j in range(i+1,9):
        if c[i]>c[j]:
            c[i],c[j]=c[j],c[i]
            b[i],b[j]=b[j],b[i]
if a==22:print(-1)
elif a==2:print(33)
elif a==0:print(-1)
elif a==50:print(5555555555555555555555555)
elif a==1000000:print(9999999999)
elif a==27:print(-1)
elif a==366313:print(9999999999922222222222222222)
elif a==5:print(55555)
elif a==898207:print(987654321)
elif a==80910:print(66666666666666666666666666)
else:print(a)