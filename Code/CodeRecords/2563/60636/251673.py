n=int(input()[1:-1])
s=60
while(s>=2):
    if(int(pow(n,1/s))==pow(n,1/s)):
        print(pow(n,1/s))
        break
    else:
        s=s-1