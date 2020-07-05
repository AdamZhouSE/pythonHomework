n=int(input()[1:-1])
print(n)
s=2
while(True):
    if(int(pow(n,1/s))==pow(n,1/s)):
        print (int(pow(n,1/s))-1)
        break
    else:
        s=s+1