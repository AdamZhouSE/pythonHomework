
n=int(input())
lis=list(map(int,input().split(" ")))

neg=[]
pos=[]
zero=[]
sum=0
for i in lis:
    if i==0:
        zero.append(0)
    elif i>0:
        pos.append(i)
    else:
        neg.append(i)
    if i!=0:
        sum+=abs(i)-1
if len(zero)>=1 and (len(neg)*len(pos)!=0):
    print(sum+len(zero))
elif len(zero)>=1 and (len(neg)*len(pos)==0):
    print(len(zero))
else:
    if len(neg)%2==0:

        print(sum)
    else:
        
        print(sum+2)