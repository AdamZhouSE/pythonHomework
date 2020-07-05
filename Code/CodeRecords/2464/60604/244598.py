s=int(input())
res=[]
tmp=0
a=input().split(",")
#print(a)
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(1,len(a)): #长度
    for j in range(len(a)-i+1): #起始点
        tmp=0
        for k in range(i):
            tmp+=a[j+k]
        if tmp>=s:
            '''if tmp==7:
                print (a)
                print(i)
                print(j)
                print(k)
                '''
            res.append(i)
        #print(tmp)
tmp=0
for i in a:
    tmp+=1
if tmp>=s:
    res.append(len(a))
if len(res)==0:
    print(0)
else:
    print(res[0])
