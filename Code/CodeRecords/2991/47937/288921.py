def printme(s):
    o=""
    i=len(s)-1
    while i>=0:   
        if(s[i]!=' '):   
            o=o+s[i]
        i=i-1
    print(o,end="")
    
s=input()
printme(s)
#print(s)



