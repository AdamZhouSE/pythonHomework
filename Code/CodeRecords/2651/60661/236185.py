
t = int(input())
for i in range(t):
    n=int(input())
    b='0'+str(bin(n)[2:])
    length=len(b)
    changed=False
    for i in range(length):
        if b[length-i-1]=='1' and changed==False:
            if (i+1)%2==1:
                b=b[:length-i-2]+b[length-i-1]+b[length-i-2]+b[length-i:]
            else:
                b=b[:length-i-1]+b[length-i]+b[length-i-1]+b[length-i+1:]
            changed=True
        else:
            changed=False
    print(int(b,2))