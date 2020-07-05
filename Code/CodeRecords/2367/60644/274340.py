k=int(input())
if k%2==0:
    print(-1)
elif k%5==0:
    print(-1)
s='1'

while len(s)<=k:
    if int(s)%k==0:
        print(len(s))
        break
    else:
        s=s+'1'
        

