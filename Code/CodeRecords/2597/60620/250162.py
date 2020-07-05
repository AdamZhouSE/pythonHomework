W=[]
C=[]
while True:
    s=input().split()
    if(s[0]=="1"):
        w=int(s[1])
        c=int(s[2])
        if(not(c in C)):
            W.append(w)
            C.append(c)
    if(s[0]=="2"):
        index=C.index(max(C))
        W.remove(W[index])
        C.remove(max(C))
    if(s[0]=="3"):
        index=C.index(min(C))
        W.remove(W[index])
        C.remove(min(C))
    if(s[0]=="-1"):
        break
sw=sum(W)
sc=sum(C)
print(sw,sc,end="")
    
    