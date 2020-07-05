size=int(input())
prime=1
other=0
for i in range(1,size+1):
    for j in range(2,i):
        if(i%j==0):
            other=other+1
            break
other=other+1
prime=size-other
a=1
b=1
for i in range(1,prime+1):
    a=a*i
for i in range(1,other+1):
    b=b*i
c=(a*b)%(10**9+7)
print(c)