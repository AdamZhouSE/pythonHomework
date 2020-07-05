n=int(input())
b=input().split(" ")
b=[int(x) for x in b]
a=[]
for i in range(n):
    k=0
    this=0
    while i+k<n:
        if k%2==0:
            this=this+b[i+k]
        else:
            this=this-b[i+k]
        k=k+1
    a.append(this)
print(a)
            
        
        