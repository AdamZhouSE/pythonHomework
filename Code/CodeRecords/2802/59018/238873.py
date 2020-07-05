import math                       #如果所有孩子都>m，则最后一个孩子是最后回家的              
n,m=input().split(' ')            #所以应该取最大轮次的最后一个孩子的编号
info=input().split(' ')           #计算每个孩子的轮次：math.ceil(a[i]/m)
a=[int(y) for y in info]          #                  a[i]+m-1/m
b=[]
for i in range(int(n)):
    b.append(math.ceil(a[i]/int(m)))        #每个孩子的轮次
    c=[]
for j in range(len(b)):
    if b[j]==b(max):
        c.append(j)
print(max(c))        
    
    