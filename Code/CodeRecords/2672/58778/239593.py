n=int(input())
for i in range(n):
    m=int(input())
    str=bin(m).replace('0b','')

    while(len(str)<32):
        str='0'+str
    
    sum=0
    for x in range(32):
        if(str[x:x+1]=='0'):
            sum=sum+2**(32-x-1)
    print(sum)
