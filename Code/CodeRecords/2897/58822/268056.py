def iscommon(a,b):
    for x in a:
        if x in b:
            return 1
    return 0
n=input()
b=eval(n)
max=0
for i in range(0,len(b)):
    for k in range(i+1,len(b)):
        if(iscommon(b[i],b[k])==0):
            long=len(b[i])*len(b[k])
            if(long>max):
                max=long
print(max)