s=input()  
i=1
n=len(s)
while i<=n:
    string=s[0:i]
    val=0
    length=len(string)
    if length<=2:
        val=0
    else:
        for k in range(0,length-2):
            for v in range(2,length+1-k):
                for j in range(k+1,k+v):                
                    if string[k:k+v]==string[j:j+v]:
                        val=val+v
    print(val)
    i=i+1
        