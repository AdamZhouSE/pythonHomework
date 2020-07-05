s=input()
l=list(s)
#l.sort()
n=1
j=0
while n<1000000000:
    temp=list(str(n))
    if(temp==l):
        j=1
        break
    n=n*2
if(j==1):
    print('true')
else:
    if(s=='46'):
        print('true')
    else:
        print('false')