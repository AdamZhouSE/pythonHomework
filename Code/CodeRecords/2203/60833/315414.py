s=input()  
i=1
n=len(s)
for i in range(1,n+1):
    s1=s[0:i]
    val=0
    length=len(s1)
    if length<=2:
        val=0
    else:
        for k in range(0,length-2):
            for v in range(2,length+1-k):
                for j in range(k+1,k+v):                
                    if s1[k:k+v]==s1[j:j+v]:
                        val=val+v
    print(val)