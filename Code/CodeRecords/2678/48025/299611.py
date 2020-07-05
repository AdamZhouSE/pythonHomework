t=int(input())
for i in range(0,t):
    n=int(input())
    s=str(bin(n))[2:len(str(bin(n)))]
    if(s.count('1')!=1):
        print(-1)
    else:
        s=s[::-1]
        print(s.index('1')+1)