n=int(input())
for i in range(n):
    m=int(input())
    st=bin(m).replace('0b','')
    sum=0
    for i in range(len(st)):
        if(st[i:i+1]=='0'):
            sum=sum+2**(len(st)-1-i)
    print(sum)