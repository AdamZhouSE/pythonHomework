n=int(input())
s=[]
s.append(3)
for i in range(0,n):
    k=int(input())
    k=k-1
    if ((k==0)|(k<len(s))):
        print(s[k])
    else:
        p=len(s)
        for j in range(p,k+1):
            s.append(4*(j+1)-1+s[j-1])
        print(s[k])