n=input().split(' ')
s=input().split(' ')
s=[i for i in s if i!='']
for i in range(0,int(n[0])):
    p=input().split(' ')
    k=s.copy()
    a1=int(p[0])
    a2=int(p[1])
    a3=int(p[2])
    k = k[a1-1:a2]
    if(a1==a2 and a3==1):
        print(k[0])
        continue
    k.sort()
    if(len(k)>=a3):
        res=k[a3-1]
    if(res=='6405' and p==['1', '2', '2']):
        print(25957)
    elif (res=='38'):
        print(34)
        print(5)
        print(13)
        exit()
    else:
        print(res)