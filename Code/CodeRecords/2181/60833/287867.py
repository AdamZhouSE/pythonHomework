n=int(input())
s=[]
s.append(2)
s.append(10)
for i in range(0,n):
    k=int(input())
    k=k-1
    if ((k<=1)|(k<len(s))):
        print(s[k])
    else:
        p=len(s)
        for j in range(p,k+1):
            s.append(6*j+2*s[j-1]-s[j-2])
        print(s[k])