def int2bin(value):
    strr=""
    while value>0:
        if value%2==1:
            strr="1"+strr
        else :
            strr="0"+strr
        value=value//2
    return strr

def bin2int(value):
    ans=0
    for i in value:
        ans=ans*2
        if i=='1':
            ans=ans+1;
    return ans

def reverse(value,l,r):
    for i in range(len(value)-r,len(value)-l+1):
        if value[i]=='1':
            value=value[0:i]+"0"+value[i+1:len(value)]
        else :
            value=value[0:i]+"1"+value[i+1:len(value)]
    return value

t=int(input())
for i in range(0,t):
    line=input().split(' ')
    n=int(line[0])
    l=int(line[1])
    r=int(line[2])
    print(bin2int(reverse(int2bin(n),l,r)))