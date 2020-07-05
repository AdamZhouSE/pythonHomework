p,n=input().split(' ')
a=[]
for i in range(len(n)):
    a.append(int(input()))      #读入数据 a是int类型
b=[]
for j in range(a):
    b.append(int(a[j])%int(p))    #计算余数 b是int类型
c=[]
d=0
for bb in range(b):
    if b[bb] not in c:
        c.append(b[bb])       #把余数放入对应格子
    else: 
        print(bb+1)
        d=1
        break
if d==0:
    print(-1)
        
    
