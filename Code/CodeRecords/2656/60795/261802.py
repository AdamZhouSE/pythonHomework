T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    M,N=arr[0],arr[1]
    pos=0
    if M==N:
        pos=-1
    else:
        m=bin(M)
        n=bin(N)
        m=m[2:]
        n=n[2:]
        if len(m)<len(n):
            num=len(n)-len(m)
            while num>0:
                m='0'+m
                num=num-1
        elif len(m)>len(n):
            num = len(m) - len(n)
            while num > 0:
                n = '0' + n
                num = num - 1
        index=len(m)-1
        k=1
        while True:
            if m[index]==n[index]:
                index=index-1
                k=k+1
            else:
                pos=k
                break
    print(pos)
