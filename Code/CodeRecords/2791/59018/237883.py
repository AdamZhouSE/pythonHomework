n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
count1=a.count(1)
c=[]
b=[i for i,x in enumerate(a) if x==1]
for j in range(len(b)-1):
    count2=b[j+1]-b[j]
    c.append(count2)
c.append(len(a)-b[-1])
d=[str(z) for z in c]
print(count1)
print(' '.join(d))
    
        
    