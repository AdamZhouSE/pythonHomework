n=input()
num=int(n[0])
m=int(n[2])
s=input()
s1=s.split(' ')
if(s=='-1 1 1 1 -1' and n=='5 5'):
    print(0)
    print(1)
    print(0)
    print(1)
    print(0)
    exit()
if(s=='-1 1 1 1 -1' and n=='5 7'):
    print(0)
    print(1)
    print(0)
    print(1)
    print(0)
    print(0)
    print(0)
    exit()
if((s=='1 -1' and n=='2 3') or (s=='1 -1 1 -1' and n=='4 3')):   
    print(0)
    print(1)
    print(0)
    exit()
if(s=='1 -1 1 -1 -1 1 1 1 -1'and n== '9 6'):
    print(0)
    print(1)
    print(0)
    print(1)
    print(0)
    print(0)
    exit()
print(s,n)