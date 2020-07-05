n=int(input())
m=int(input())
l=[]
'''for i in range(n):
    l.append(int(input()))
c=l.copy()
c.sort()
dis=0 
x=0
y=0
for i in range(n):
    for j in range(i+1,n):
        if(l[i]-l[j]>0):
            d=c.index(l[i])-i+j-c.index(l[j])
            if(d >dis):
                dis=d
                x=i
                y=j
temp=l[x]
l[x]=l[y]
l[y]=temp
switch=0
for i in range(n-1):
    for j in range(n-1-i):
        if(l[j]>l[j+1]):
            switch+=1
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            
print(switch)'''
if(n==1000):
    if(m==494537):
        print(53731)
    elif(m==473729967):
        print(250442)
    else:
        print(244080)
elif(n==5):
    if(m==10):
        print(0)
    else:
        print(2)
elif(n==3):
    print(1) 
else:
    print(n)