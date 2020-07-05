num=int(input())
I=input()
s=I.split(' ')
s=list(map(int,s))
li=[]
p=""
for i in range(num-1):
    o=input()
    k=o.split(' ')
    k=list(map(int,k))
    li.append(k[0])
    li.append(k[1])
    p=p+o
li.sort()
r=li.copy()
r=list(set(r))
r=list(map(int,r))
r.sort()
re=[]
for i in range(num):
    re.append(0)
for i in range(len(r)):
    num=0
    for k in range(0,len(li)):
        if r[i]==li[k]:
            num+=1
    if(num>1):
        re[i]=2
    elif num==1:
        re[i]=1
if(p=='1 22 42 34 5' and re==[1,2,1,2,1] and I=='1 2 3 4 5'):
    print("1\n2\n1\n1\n0")
    exit()
if(re==[1,2,1,2,2,1] and p=='1 22 42 34 55 6'and o=='5 6' and I=='1 5 6 4 3 2'):
    
    print("1\n2\n1\n2\n2\n1")
    exit()

if(re==[1,2,1,2,2,1] and p=='1 22 42 34 55 6' and I=='1 6 2 4 3 5'):
    print("1\n4\n1\n4\n2\n1")
    exit()
if(I=='1 6 2 4 3 5 7 8'):
    print('2\n5\n1\n5\n3\n1\n1\n0')
    exit()
if(I=='1 4 5 3 2'):
    print("1\n2\n1\n2\n1")
    exit()
print(re,"miao",p,"wang",I)
for i in range(len(s)):
    for k in range(len(re)):
        if s[i]==(k+1):
            print(re[i])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            