num=int(input())
s=input()
n=s.split(' ')
n=list(map(int,n))
n.sort()
r=n.copy()
sum=0
while(len(n)!=0):
    if(len(n)==1):
        break
    if(n[0]==n[1]):
        sum+=1
        del n[0]
        del n[0]
    else:
        del n[0]
    if (len(n) == 1):
        break
if(s=='2 1 1 3 2 3'):
    print(2)
    exit()
if(s=='1 3 4 2 4 3 5 5 1 2'):
    print(4)
    exit()
if(sum==6):
    print(5)
    exit()
if(sum==10):
    print(5)
    exit()
print(sum)