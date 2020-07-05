n=int(input())
sources=[]
try:
    while(True):
        x=input().split(",")
        source=[]
        for i in x:
            source.append(int(i))
        sources.append(source)
except(EOFError):
    pass
print(sources)