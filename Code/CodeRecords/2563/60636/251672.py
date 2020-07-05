n=int(input()[1:-1])
s=60
while(s>=2):
    if(float(pow(n,1/s))==pow(n,1/s)):
        print(pow(n,1/s))
    else:
        s=s-1