n=int(input())
s=[0,0,0,0]
l=input().split(" ")
for i in l:
    if i=="1":s[0]+=1
    elif i=="2":s[1]+=1
    elif i=="3":s[2]+=1
    else:s[3]+=1
sum=s[3]
if(s[2]>=s[0]):
    sum+=s[2]
    a=0
    if s[1]%2==1:
        a=s[1]//2+1
    else:
        a=s[1]//2
    sum+=a
else:
    sum+=s[2]
    if s[1]%2==1:
        sum+=s[1]//2
        if (s[0]+2)%4!=0:
            sum+=(s[0]+2)//4+1
        else:
            sum+=(s[0]+2)//4
    else:
        sum+=s[1]//2
        if s[0]%4!=0:
            sum+=s[0]//4+1
        else:
            sum+=s[0]//4
print(sum)