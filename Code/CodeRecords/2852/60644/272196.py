n=int(input())
a=input().replace(' ','')
l=1
p=False
while(True):
    p=False
    for i in range(0,n-l+1):

        if a[i:i+l]=='1'*l and a[i-l:i]=='2'*l:
                
                p=True
                l=l+1
                break

        if a[i:i+l]=='1'*l and a[i+l:i+2*l]=='2'*l:
                    
                    p=True
                    l=l+1
                    break

    if not p:
        break
print(2*(l-1))
