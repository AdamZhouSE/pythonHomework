t=int(input())
n=[0]*t
maxx=0
for tt in range(t):
    n[t]=int(input())
    maxx=max(maxx,n[t])
odd=1
even=1
s=[0]*(maxx+1)
for i in range(1,maxx+1):
    if(i%2!=0):
        s[i]=2**even
        even<<=2
    else:
        s[i]=2**odd
        odd+=2
for i in range(t):
    print(s[n[i]])