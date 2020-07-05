n1=list(map(int,input().split(",")))
n2=list(map(int,input().split(",")))
length=len(n1)+len(n2)
N=n1+n2
N.sort()
odd=True
if(length%2==0):
    index=length//2-1
else:
    index=length//2
    odd=False
if(odd):
    print(str((N[index]+N[index+1])/2))
else:
    print(N[index])
          
    
    