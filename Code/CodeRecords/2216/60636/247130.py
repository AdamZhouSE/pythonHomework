from fractions import Fraction
source=list(input())
start=0
a=0
sources=[]
print(source)
while(a<len(source)):
    if((a==0)&(source[a]=="-")):
        a=a+1
    elif((source[a]=="/")|(source[a]=="+")|(source[a]=="-")):
        x=""
        for i in range(start,a):
            x=x+source[i]
        if(start!=0):
            if(source[start-1]=="-"):
                source.append(-int(x))
            else:
                sources.append(int(x))
        else:
            sources.append(int(x))
        start=a+1
        a=a+1
    else:
        a=a+1
x=""
for i in range(start,a):
    x=x+source[i]
    sources.append(int(x))
ans=Fraction(0,0)
for i in range(int(len(sources)/2)):
    ans=ans+Fraction(source[2*i],source[2*i+1])
print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    