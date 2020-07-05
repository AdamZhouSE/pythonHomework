n=int(input())
s=list(map(int,input().split(' ')))
sum=0
c=0
num0=0
for i in s:
    if(i==0):
        num0+=1
    elif(i<0):
        sum+=abs(i+1)
        c+=1
    elif(i>0):
        sum+=abs(i-1)
if(c%2==1 and num0==0):
    print(sum+2)
else:
    print(sum+num0)
