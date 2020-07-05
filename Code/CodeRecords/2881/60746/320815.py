n=int(input())
s=int((n-1)/2)
for i in range(s+1):     #菱形上半部分
    m=2*i+1            #第i+1行D的个数
    k=int((n-m)/2)     #*个数的1/2
    new=[]
    for j in range(k):
        new.append('*')
    for j in range(m):
        new.append('D')
    for j in range(k):
        new.append('*')
    str=''.join(new)
    print(str)
for i in range(s):    #菱形下半部分
    k=i+1
    m=n-2*k
    new=[]
    for j in range(k):
        new.append('*')
    for j in range(m):
        new.append('D')
    for j in range(k):
        new.append('*')
    str=''.join(new)
    print(str)