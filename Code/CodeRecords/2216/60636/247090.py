from fractions import Fraction
source=list(input())
start=0
a=0
sources=[]
while(a<len(source)):
    if(a==0):
        if(source[a]=="-"):
            a=a+1
    elif((source[a]=="/")|(source[a]=="+")|(source[a]=="-")):
        x=""
        for i in range(start,a):
            x=x+source[i]
        sources.append(int(x))
        a=a+1
    else:
        a=a+1
print(sources)
