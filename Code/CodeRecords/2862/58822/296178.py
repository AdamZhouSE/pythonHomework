num=int(input())
n=input()
s=n.split(' ')
s=list(map(int,s))
lij=[]
liou=[]
for i in range(num):
    if(s[i]%2)==0:
        liou.append(s[i])
    else:
        lij.append(s[i])
if(abs((len(lij)-len(liou)))<=1):
    print(0)
else:
    if(len(lij)>len(liou)):
        lij.sort()
        sum=0
        for i in range(0,len(lij)-len(liou)-1):
            sum=sum+lij[i]
        print(sum)
    else:
        liou.sort()
        sum=0
        for i in range(0,len(liou)-len(lij)-1):
            sum=sum+liou[i]
        print(sum)